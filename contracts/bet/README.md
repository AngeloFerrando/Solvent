# Bet

## Specification

The contract is a bet between two players, who bet 1 ETH each. An oracle chooses the winner of the pot, by calling a `win` method that transfers the pot to the chosen winner.

The contract involves the following steps: 
- `player1` deploys the contract by depositing 1 ETH as a bet;
- then, `player2` can bet 1 ETH by calling the `join` method;
- if `player2` does not join by `deadline`, then `player1` can redeem the bet;
- once both players have joined, the oracle chooses the winner, which receives the 2 ETH;
- after `deadline`, it is only possibile for both players to take their bets back.

## Properties

- **any_timeout_join**: if `deadline` has passed and `player2` has not joined, then anyone can make `player1` redeem the bet
- **any_timeout_win**: if `deadline` has passed and the oracle has not chosen the winner, then anyone can make the players redeem their bets
- **oracle_win**: once `player2` has joined and before `deadline`, the oracle can transfer the pot to one of the players
- **no_frozen_funds**: once the players have redeemed their bets, the contract is liquid, namely any participant can withdraw the whole contract balance
