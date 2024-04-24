# Lottery

## Specification

Consider a lottery where 2 players bet 1 ETH each, and the winner - who is chosen fairly between the two players - redeems the whole pot.

Since smart contract are deterministic and external sources of randomness (e.g., random number oracles) might be biased, to achieve fairness we follow a *commit-reveal-punish* protocol, where both players first commit to the secret hash, then reveal their secrets (which must be preimages of the committed hashes), and finally the winner is computed as a fair function of the secrets.

Implementing this properly is quite error-prone, since the protocol must prescribe punishments in case a player behaves dishonestly, e.g. by refusing to perform some required action. In this case, the protocol must still ensure that, on average, an honest player has at least the same payoff that she would have by interacting with another honest player. 

The protocol followed by the players is the following:
- `player1` joins the lottery by paying 1 ETH and committing to a secret;
- `player2` joins the lottery by paying 1 ETH and committing to another secret;
- if `player2` has not joined, `player1` can redeem her bet after block `end_commit`; 
- once both secrets have been committed, `player1` reveals the first secret;
- if `player1` has not revealed, `player2` can redeem both players' bets after block `end_reveal`; 
- once `player1` has revealed, `player2` reveals the secret;
- if `player2` has not revealed, `player1` can redeem both players' bets after block `end_reveal+100`;
- once both secrets have been revealed, the winner, who is determined as a function of the two revealed secrets, can redeem the whole pot of 2 ETH.

## Properties

- **anyone_anystate_wd**: in any state, any user can withdraw the whole contract balance (should be false)
- **p1_anystate_wd**: in any state, player1 can withdraw the whole contract balance (should be false)
- **p1_redeem_nojoin**: in state 1, player1 can redeem at least her bet after the block `end_commit`
- **p2_redeem_noreveal**: in state 2, player2 can redeem at least both players' bets after the block `end_reveal`
- **anyone_liquid3**: in state 3, anyone can withdraw the whole contract balance
- **player1_redeem_noreveal**: in state 4, player1 can redeem at least both players' bets after the block `end_reveal`
- **one_player_win**: in state 5, either player1 or player2 can redeem at least both players' bets
