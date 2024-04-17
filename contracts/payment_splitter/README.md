# Payment Splitter

## Specification 

This contract allows to split payments among a group of accounts in any arbitrary proportion. 

The contract has an initialization phase, where the owner can set the shares of each account through the function `addShares`. The owner can finalize this phase by calling the function `finalizeShares`. 

After that, the function `release` allows anyone to transfer funds from the contract to an account. Each account will can receive an amount of ETH proportional to the percentage of total shares.

The contract can receive ETH at any time through the function `receive`.

## Properties

