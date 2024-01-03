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