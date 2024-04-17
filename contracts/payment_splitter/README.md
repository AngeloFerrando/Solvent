# Payment Splitter

## Specification 

This contract allows to split payments among a group of accounts.

The split can be in any arbitrary proportion. The way this is specified is by assigning a number of shares to each account. Each account will then be able to claim an amount proportional to the percentage of total shares. The distribution of shares is set at the time of contract deployment.
