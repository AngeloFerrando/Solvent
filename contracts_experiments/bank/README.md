# Bank

The Bank contract stores assets deposited by users, and and pays them out when required. The `deposit` method allows anyone to deposit assets. When a deposit is made, the corresponding amount is added to the account balance of the sender. The `withdraw` method allows the sender to receive any desired amount of assets deposited in their account. The contract checks that the depositor has sufficient funds in their account and then transfers the specified amount to the sender.

## Properties
- **deposit_not_revert**: a `deposit` call does not revert if `msg.value` is less or equal to the ETH balance of `msg.sender`.
- **withdraw_not_revert**: if A has a non-zero deposit in the bank, then A can withdraw the full deposit in a single transaction
