Automatic Tx Machine 🏧
========================

[![Tests](https://github.com/nucypher/ATxM/actions/workflows/pytest.yml/badge.svg)](https://github.com/nucypher/ATxM/actions/workflows/pytest.yml)

An async EVM transaction retry machine.
Programmatically queue, broadcast, and retrying (speedup) transactions.
Transactions are queued and broadcasted in a first-in-first-out (FIFO) order.

The machine is designed to be used in a long-running process, like a server.

[![Diagram](./diagram.png)](./diagram.png)

### Installation

```bash
pip install atxm
```

### Usage

```python
from eth_account.local import LocalAccount
from web3 import Web3, HTTPProvider
from atxm import AutomaticTxMachine
from twisted.internet import reactor


account = LocalAccount.from_keyfile('path/to/keyfile', 'password')
w3 = Web3(HTTPProvider("http://localhost:8545"))

transaction = {
    'chainId': 80001,
    'to': '0x1234567890123456789012345678901234567890',
    'nonce': 0,
    'value': 0,
    'gas': 21000,
    'maxFeePerGas': '1',
    'maxPriorityFeePerGas': '1',
}

machine = AutomaticTxMachine(w3=w3)
future_tx = machine.queue_transaction(
    signer=account,
    params=transaction,
    on_broadcast_failure=...,
    on_fault=...,
    on_finalized=...,
    on_insufficient_funds=...,
)

reactor.run()
```

### Features


##### Futures

The tracker returns a `FutureTx` instance when a transaction is queued.
The FutureTx instance can be used to track the transaction's lifecycle and
to retrieve the transaction's receipt when it is finalized.

##### Retry Strategies

The tracker supports a generic configurable interface for retry strategies (`AsynxTxStrategy`).
These strategies are used to determine when to retry a transaction and how to do so.
They can be configured to use any kind of custom context, like gas oracles.

##### Lifecycle Hooks 

Hooks are fired in a dedicated thread for lifecycle events.

- `on_broadcast` _(Optional)_: When a transaction is broadcasted.
- `on_broadcast_failure`: When a transaction fails to broadcast.
- `on_finalized`: When a transaction is finalized (successful or reverted).
- `on_fault`: When a transaction error occurred.
- `on_insufficient_funds`: When the account associated with the transaction does not have enough funds for the transaction.


##### Crash-Tolerance

Internal state is written to a file to help recover from crashes
and restarts. Internally caches LocalAccount instances in-memory which in
combination with disk i/o is used to recover from async task restarts.


##### Throttle 

There are three rates, work (fast scan), idle (slow scan) and sleep (zero activity).
This reduces the use of resources when there are no transactions to track.
When a transaction is queued, the machine wakes up and goes to work.
When all work is complete it eases into idle mode and eventually goes to sleep.

##### Event Loop Support

Currently, the machine is designed to work with the Twisted reactor.
However, it can be adapted to work with any event loop.
