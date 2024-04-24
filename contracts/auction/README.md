# Auction

## Specification

The Auction contract allows a seller to create an auction. In the constructor, the seller must specify:
- its own address (`seller`),
- the `deadline` of the auction,
- the minimum bid (`min_bid`) of the auction,

After creation, the following actions are possible:
- `bid`: after the auction starts, any user can bid an amount of ETH by transferring that amount to the contract. In the event of a raise, the contract returns the old maximum bid to the user who paid it;
- `close`: after the deadline, the seller can close the auction, and withdraw the highest bid. 

## Properties

- **seller_wd**: the seller can withdraw the current bid (greater than 0) after the deadline
- **old_winner_wd**: the old winner can withdraw the current bid
- **seller_wd2**: the seller can withdraw the bid (greater than the minimum bid) after the deadline
- **seller_wd_early**: the seller can always withdraw something (should be false before the deadline) 
- **seller_wd_closed**: the seller can withdraw something in any state (should be false: the contract can be already closed)
- **seller_wd_nowinner**: the seller can withdraw something in any state (should be false: if the winner has not been set, the contract balance could be 0)
- **nonseller_wd**: the `close` transaction can be fired by someone who is not the seller (should be false)
- **liquidity**: the extra budget can always be redeemed by the seller



