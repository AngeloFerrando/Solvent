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
make compile Contract=<file.sol> N_Transactions=<number of transitions> N_Participants=<number of participants> LOGIC=<logic to use in the SMT>
```

```bash
make run SMT=<smt solver>
```

## Example of use with Make

```bash
make compile Contract=./examples/liquidity2.sol N_Transactions=4 N_Participants=2 LOGIC="(set-logic LIA)"
```

```bash
make run SMT=z3
```
