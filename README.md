# Solvent

A tool to formally verify smart contracts through SMT solvers.

## How to install

- [Step 1] Install Z3, this can be done following the documentation at https://github.com/Z3Prover/z3
- [Optional step] Other SMT solvers can be installed as well, like cvc5 (https://cvc5.github.io/), and so on 
- [Step 2] Install Python 3, this can be done following the documentation at https://www.python.org/
- [Step 4] Install Pip, this can be done following the documentation at https://pypi.org/project/pip/
- [Step 5] Install through Pip all Solvent's requirements
```bash
pip3 install -r requirements.txt
```
- [Optional step] In case the grammar needs to be extended, install Antlr4 (this is not necessary to use the tool, but only to extend it), this can be done following the documentation at https://www.antlr.org/ (install version 4.7.2); once this is done, run the following to compile the extended grammar
```bash
antlr4 -Dlanguage=Python3 -visitor TxScript.g4 
```

## To test the tool on the benchmarks

```bash
cd contracts
python3 test.py
```

## How to use with Make

The tool can be executed directly from the main Python script, however, it is better to compile the contract and run the verification with the available makefiles.

Each contract has a Makefile, such a file can be used to compile and run the verification. To compile the smart contract, it is enough to execute the following

```bash
make compile Contract=<file.sol> N_Transactions=<number of transitions> N_Participants=<number of participants> Can_Transactions_Arrive_Any_time=<True or False>
```

Note that, Can_Transactions_Arrive_Any_time is optional (when not passed to the makefile it is assumed to be True).

After that, to run the verification it is enought to execute the following

```bash
make run SMT=<smt solver>
```

Note that, smt solver can be any SMT solver installed on the machine (e.g., z3, or cvc5, and so on).

## Example of use with Make

To compile a SOL file into its SMT version

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

## To create a new contract

- [Step 1] Create a new folder inside the contracts folder (or any other place on the machine). 
- [Step 2] Create a .sol file in the previously created folder.
- [Step 3] Copy any of the Makefile available in the other contracts inside this folder.
- [Optional Step] Change the Makefile so copied if needed, usually it is enough to change line 11, to set the default contract name to the .sol contract created in the folder.
- Compile the contract and Run the verification as for all the other contracts in the repository.