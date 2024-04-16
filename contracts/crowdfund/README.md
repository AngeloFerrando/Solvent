# Crowdfund

## Specification

The Crowdfund contract implements a crowdfunding campaign. 

The constructor specifies the `owner` of the campaign, the `deadline` for receiving donations, the minimum amount for donations, and the `target` that must be reached for the campaign to be successful. 

The contract implements the following functions:
- `donate`, which allows anyone to deposit any amount of tokens in the contract. Donations are only possible before the donation period has ended;
- `wdOwner`, which allows the `owner` to redeem all the tokens deposited in the contract. This is only possible if the campaign `target` has been reached;   
- `wdDonor`, which allows donors to reclaim their donations after the donation period has ended.

## Properties
- **owner_wd**: if threshold is reached, the owner can withdraw at least the target after the deadline
- **donor_wd**: if threshold is not reached, donors can withdraw their donations after the deadline
- **liquidity**: the extra budget can always be redeemed by the owner