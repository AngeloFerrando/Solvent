# Bet

## Specification
The contract involves two players, each owning 1 token, and an oracle. Player 1 initiates the contract by depositing its token. Then, player 2 can deposit its token. Once both players have deposited their token, the oracle chooses the winner, which receives the 2 tokens. After a given time limit, it is only possibile for both players to take their tokens back, if any.

## Properties
- **liq1**: before the deadline, if the contract balance is 2 then the oracle has a 5-steps strategy to increase the balance of player 1 or player 2 of at least 2 tokens. 

## Versions
- **v1**: compliant with the specification.
- **v2**: uses token balances (unreliable!) to infer contract state.