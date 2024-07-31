import json
import time
from collections import deque
from copy import copy
from json import JSONDecodeError
from pathlib import Path
from typing import Callable, Deque, Dict, Optional, Set, Tuple, Union

from web3.types import TxParams, TxReceipt

from atxm.exceptions import InsufficientFunds, TransactionFaulted
from atxm.logging import log
from atxm.tx import (
    FaultedTx,
    FinalizedTx,
    FutureTx,
    PendingTx,
    TxHash,
)
from atxm.utils import fire_hook


class _TxTracker:
    """State management for transaction tracking."""

    _FILEPATH = ".txs.json"
    __COUNTER = 0  # id generator

    def __init__(self, disk_cache: bool, filepath: Optional[Path] = None):
        self.__filepath = filepath or self._FILEPATH

        self.__queue: Deque[FutureTx] = deque()
        self.__active: Optional[PendingTx] = None
        self.finalized: Set[FinalizedTx] = set()

        self.disk_cache = disk_cache
        if disk_cache:
            self.restore()

    def to_dict(self) -> Dict:
        """Serialize the state to a JSON string."""
        active = self.__active.to_dict() if self.__active else {}
        queue = [tx.to_dict() for tx in self.__queue]
        finalized = [tx.to_dict() for tx in self.finalized]
        _dict = {"queue": queue, "active": active, "finalized": finalized}
        return _dict

    def commit(self) -> None:
        """Write the state to the cache file."""
        if not self.disk_cache:
            return
        with open(self.__filepath, "w+t") as file:
            data = json.dumps(self.to_dict())
            file.write(data)
        log.debug(f"[tracker] wrote transaction cache file {self.__filepath}")

    def restore(self) -> bool:
        """
        Restore the state from the cache file.
        Returns True if the cache file exists and was successfully
        restored with data.
        """
        if not self.disk_cache:
            return False

        # read & parse
        if not self.__filepath.exists():
            return False
        with open(self.__filepath, "r+t") as file:
            data = file.read()
        try:
            data = json.loads(data)
        except JSONDecodeError:
            data = dict()
        active = data.get("active", dict())
        queue = data.get("queue", list())
        final = data.get("finalized", list())

        # deserialize & restore
        self.__active = PendingTx.from_dict(active) if active else None
        self.__queue.extend([FutureTx.from_dict(tx) for tx in queue])
        self.finalized = {FinalizedTx.from_dict(tx) for tx in final}
        log.debug(
            f"[tracker] restored {len(queue)} transactions from cache file {self.__filepath}"
        )

        return bool(data)

    def __set_active(self, tx: PendingTx) -> None:
        """Update the active transaction (destructive operation)."""
        old = None
        if self.__active:
            old = self.__active.txhash
        self.__active = tx
        self.commit()
        if old:
            log.debug(
                f"[tracker] updated active transaction {old.hex()} -> {tx.txhash.hex()}"
            )
            return
        log.debug(f"[tracker] tracked active transaction {tx.txhash.hex()}")

    def __pop(self) -> FutureTx:
        """Pop the next transaction from the queue."""
        return self.__queue.popleft()

    def update_active_after_successful_strategy_update(
        self, tx: PendingTx
    ) -> PendingTx:
        if not self.__active:
            raise RuntimeError("No active transaction to update")
        if tx.id != self.__active.id:
            raise RuntimeError(
                f"Mismatch between active tx ({self.__active.id}) and provided tx ({tx.id})"
            )

        self.__active.txhash = tx.txhash
        self.__active.params = tx.params
        self.__active.last_updated = int(time.time())
        self.__active.retries = 0  # reset retries to 0

        return self.pending

    def update_active_after_failed_strategy_update(self, tx: PendingTx):
        if not self.__active:
            raise RuntimeError("No active transaction to update")
        if tx.id != self.__active.id:
            raise RuntimeError(
                f"Mismatch between active tx ({self.__active.id}) and provided tx ({tx.id})"
            )
        self.__active.retries += 1
        # safety check
        if tx is not self.__active:
            tx.retries = self.__active.retries

    def morph(self, tx: FutureTx, txhash: TxHash) -> PendingTx:
        """
        Morphs a future transaction into a pending transaction.
        Uses polymorphism to transform the future transaction into a pending transaction.
        """
        head_tx = self.head()
        if tx.id != head_tx.id:
            raise RuntimeError(
                f"Mismatch between tx at the front of the queue ({head_tx.id}) and provided tx ({tx.id})"
            )
        tx.txhash = txhash
        now = int(time.time())
        tx.created = now
        tx.last_updated = now
        tx.retries = 0  # reset retries
        tx.capped = False
        tx.__class__ = PendingTx
        tx: PendingTx

        self.__pop()  # remove from queue
        self.__set_active(tx=tx)  # set as active
        return tx

    def fault(
        self,
        fault_error: TransactionFaulted,
    ) -> None:
        """Fault the active transaction."""
        if not self.__active:
            raise RuntimeError("No active transaction to fault")
        if fault_error.tx.id != self.__active.id:
            raise RuntimeError(
                f"Mismatch between active tx ({self.__active.id}) and faulted tx ({fault_error.tx.id})"
            )

        hook = self.__active.on_fault

        tx = self.__active
        txhash = tx.txhash.hex()

        tx.fault = fault_error.fault
        tx.error = fault_error.message
        tx.__class__ = FaultedTx
        tx: FaultedTx

        log.warn(
            f"[tracker] transaction #atx-{tx.id} faulted with '{tx.fault.value}'; "
            f"{txhash}{f' ({fault_error.message})' if fault_error.message else ''}"
        )
        self.clear_active()
        fire_hook(hook=hook, tx=tx)

    def finalize_active_tx(self, receipt: TxReceipt) -> None:
        """
        Finalizes a pending transaction.
        Use polymorphism to transform the pending transaction into a finalized transaction.
        """
        if not self.__active:
            raise RuntimeError("No pending transaction to finalize")

        self.__active.receipt = receipt
        self.__active.__class__ = FinalizedTx
        tx = self.__active
        hook = self.__active.on_finalized
        self.finalized.add(tx)  # noqa
        log.info(f"[tracker] #atx-{tx.id} pending -> finalized")
        self.clear_active()
        fire_hook(hook=hook, tx=tx)

    def clear_active(self) -> None:
        """Clear the active transaction (destructive operation)."""
        self.__active = None
        self.commit()
        log.debug(
            f"[tracker] cleared 1 pending transaction \n"
            f"[tracker] {len(self.queue)} queued "
            f"transaction{'s' if len(self.queue) != 1 else ''} remaining"
        )

    @property
    def pending(self) -> Optional[PendingTx]:
        """Return the active pending transaction if there is one."""
        return copy(self.__active)

    @property
    def queue(self) -> Tuple[FutureTx, ...]:
        """Return the queue of transactions."""
        return tuple(self.__queue)

    def head(self) -> FutureTx:
        return self.__queue[0]

    def increment_broadcast_retries(self, tx: FutureTx) -> None:
        tx.retries += 1
        self.commit()

    def reset_broadcast_retries(self, tx: FutureTx) -> None:
        tx.retries = 0
        self.commit()

    def queue_tx(
        self,
        params: TxParams,
        on_broadcast_failure: Callable[[FutureTx, Exception], None],
        on_fault: Callable[[FaultedTx], None],
        on_finalized: Callable[[FinalizedTx], None],
        on_insufficient_funds: Callable[
            [Union[FutureTx, PendingTx], InsufficientFunds], None
        ],
        info: Dict[str, str] = None,
        on_broadcast: Optional[Callable[[PendingTx], None]] = None,
    ) -> FutureTx:
        """Queue a new transaction for broadcast and subsequent tracking."""
        tx = FutureTx(
            id=self.__COUNTER,
            params=params,
            info=info,
        )

        # configure hooks
        tx.on_broadcast_failure = on_broadcast_failure
        tx.on_fault = on_fault
        tx.on_finalized = on_finalized
        tx.on_broadcast = on_broadcast
        tx.on_insufficient_funds = on_insufficient_funds

        self.__queue.append(tx)
        self.commit()
        self.__COUNTER += 1
        log.info(
            f"[tracker] queued transaction #atx-{tx.id} priority {len(self.__queue)}"
        )
        return tx

    def remove_queued_tx(self, tx: FutureTx) -> bool:
        try:
            self.__queue.remove(tx)
            return True
        except ValueError:
            return False
