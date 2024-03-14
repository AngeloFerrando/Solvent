# Bank

The Bank contract accepts deposits and withdrawals from any address. When a deposit is made, the corresponding amount is added to the account balance of the depositing address. These balances are maintained using a mapping within the contract. To withdraw funds, a user can call the withdraw function of the Bank contract with a specified amount. The contract verifies that the depositor has sufficient funds in their account and then initiates a transfer of the specified amount to the depositor's address.

## Properties
- **liq1**: if A has a non-zero deposit in the bank, then A can withdraw the full deposit in a single transaction