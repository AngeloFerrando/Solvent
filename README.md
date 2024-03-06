# txscript-z3

```bash
python3 main.py <file.sol> <number of transitions> <number of participants> > output.py
```

## To test examples

```bash
./test.sh <number of transiations> <number of participants>
```

## Run Antlr4

```bash
antlr4 -Dlanguage=Python3 -visitor TxScript.g4 
```

## Requirements
antlr4-python3-runtime version 4.7.2

## How to use with Make

```bash
make compile Contract=<file.sol> N_Transactions=<number of transitions> N_Participants=<number of participants> LOGIC=<logic to use in the SMT> Can_Transactions_Arrive_Any_time=<True or False>
```

Note that, Can_Transactions_Arrive_Any_time is optional (when not passed to the makefile it is assumed to be True).

```bash
make run SMT=<smt solver>
```

## Example of use with Make

To compile a SOL file into its SMT version

```bash
make compile Contract=./examples/liquidity2.sol N_Transactions=4 N_Participants=2 
```

(Optional) To set the logic to be used with the SMT solver

```bash
make set-logic LOGIC="(set-logic LIA)"
```

To run the SMT so generated (choosing in this case Z3 as solver)

```bash
make run SMT=z3
```
