# Bet

## Specification
The contract involves two players, each owning 1 ETH, and an oracle. Player 1 initiates the contract by depositing 1 ETH as a bet. Then, player 2 can bet 1 ETH by calling the `join` method. If player2 does not join by `deadline`, then player1 can redeem the bet. Once both players have joined, the oracle chooses the winner, which receives the 2 ETH. After `deadline`, it is only possibile for both players to take their bets back.

## Properties
- **any_timeout_join**: if `deadline` has passed and player2 has not joined, then anyone can make player1 redeem the bet
- **oracle_win**: once player2 has joined and before `deadline`, the oracle can transfer the pot to one of the players
- **any_timeout_win**: if `deadline` has passed and the oracle has not chosen the winner, then anyone can make the players redeem their bets