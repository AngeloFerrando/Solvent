# Crowdfund

The Crowdfund contract implements a crowdfunding campaign. 

The constructor specifies the `owner` of the campaign, the `deadline` for receiving donations, the minimum amount for donations, and the `target` in units of token T that must be reached for the campaign to be successful. 

The contract implements the following functions:
- `deposit`, which allows anyone to deposit any amount of T in the contract. Donations are only possible before the donation period has ended;
- `wdOwner`, which allows the `owner` to redeem all the funds deposited in the contract. This is only possible if the campaign `target` has been reached;   
- `wdDonor`, which all allows donors to reclaim their donations after the donation period has ended.
