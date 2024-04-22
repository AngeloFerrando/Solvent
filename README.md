# Solvent

A tool to formally verify smart contracts through SMT solvers.

## Requirements

- [Python 3](https://www.python.org/)
- [Z3](https://github.com/Z3Prover/z3)
- [cvc5](https://cvc5.github.io/) 
- [pip](https://pypi.org/project/pip/)

## Installation

Install through pip all Solvent's requirements
```bash
pip3 install -r requirements.txt
```

To check that everything is ok, clone the repository and run the regression tests:
```bash
cd contracts
python3 test_regression.py
```

## Verifying contracts

To compile the smart contract, it is enough to execute the following

```bash
make compile Contract=<file.sol> N_Transactions=<t> N_Participants=<p> Can_Transactions_Arrive_Any_time=<true|false>
```

Note that `Can_Transactions_Arrive_Any_time` is optional (when not passed to the makefile it is assumed to be true).

After that, to run the verification as follows:
```bash
make run SMT=<smt solver>
```
Common options for `smt solver` are `z3` and `cvc5`.

For example, to verify the [Bank](contracts/bank) contract:
```bash
cd ./contracts/bank/
make compile Contract=./bank.sol N_Transactions=5 N_Participants=3
```
(Optional) To set the logic to be used with the SMT solver
```bash
make set-logic LOGIC="(set-logic LIA)"
```
To run the SMT so generated (choosing in this case Z3 as solver)
```bash
make run SMT=z3
```

## Benchmark

1. [Auction](contracts/auction)
1. [Bank](contracts/bank)
1. [Bet](contracts/bet)
1. [Crowdfund](contracts/crowdfund)
1. [Escrow](contracts/escrow)
1. [HTLC](contracts/htlc)
1. [Lottery](contracts/lottery)
1. [Payment splitter](contracts/payment_splitter)
1. [Vault](contracts/vault)
1. [Vesting wallet](contracts/vesting_wallet)

To run Solvent on the whole benchmark:
```bash
cd contracts
python3 test.py
```

## Extending Solvent

1. Create a new folder inside the contracts folder (or any other place on the machine). 
2. Create a .sol file in the previously created folder.
3. Copy any of the Makefile available in the other contracts inside this folder.
4. [Optional] Change the Makefile so copied if needed, usually it is enough to change line 11, to set the default contract name to the .sol contract created in the folder.
5. Compile the contract and Run the verification as for all the other contracts in the repository.

To extend the language supported by Solvent, install [antlr4 (version 4.7.2)](https://www.antlr.org/).
Once this is done, run the following to compile the extended grammar:
```bash
antlr4 -Dlanguage=Python3 -visitor TxScript.g4 
```