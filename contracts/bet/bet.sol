/// @custom:version compliant with the specification.

contract Bet {
  address immutable oracle;
  address immutable player1;
  int immutable deadline;

  address player2;
  int state; // 0 = JOIN-OR-TIMEOUT, 1 = WIN-OR-TIMEOUT, 2 = END
  
  constructor(address o, int d) payable {
    require (msg.value==1);
    player1 = msg.sender;
    oracle = o;
    deadline = d
  }

  function join() payable {
    require(state==0); // JOIN-OR-TIMEOUT
    require(block.number<deadline);
    require(msg.value==1);
	  require(msg.sender != player1);
    state = 1; // WIN-OR-TIMEOUT
    player2 = msg.sender
  }

  function win(address winner) {
	  require(state==1); // WIN-OR-TIMEOUT
	  require(msg.sender==oracle);
    require(block.number<deadline);
	  require(winner==player1 || winner==player2);
    state = 2; // END
    winner.transfer(balance)
  }

  function timeout() {
    require(state==0 || state==1);
   	require(block.number>=deadline);
	  player1.transfer(1);
	  if (state==1) { player2!1 };
    state = 2 // END
  }
}

// if deadline_join has passed and player2 has not joined, then anyone can make player1 redeem the bet 
property any_timeout_join_liquid {
    Forall xa
      [
        block.number>=deadline && state==0 
          -> 
        Exists tx [1, xa]
        [
          <tx>balance[player1] >= balance[player1] + 1
        ]
      ]
}

// if deadline_win has passed and the oracle has not chosen the winner, then anyone can make the players redeem their bets
property any_timeout_win_liquid {
    Forall xa
      [
        block.number>=deadline && state==1 && balance >=2 
          -> 
        Exists tx [1, xa]
        [
          (<tx>balance[player1] >= balance[player1] + 1) && 
          (<tx>balance[player2] >= balance[player2] + 1)
        ]
      ]
}

// once player2 has joined and before the deadline, the oracle can transfer the whole bet to one of the players
property oracle_win_liquid {
    Forall xa
      [
        block.number<deadline && state==1 
          -> 
        Exists tx [1, oracle]
        [
          (<tx>balance[player1] >= balance[player1] + 2) || 
          (<tx>balance[player2] >= balance[player2] + 2)
        ]
      ]
}

// once player2 has joined and before the deadline, if the contract has at least 2 ETH then the oracle can transfer the whole bet to one of the players
property oracle_win_strong_liquid {
    Forall xa
      [
        block.number<deadline && state==1 && balance>=2 
          -> 
        Exists tx [1, oracle]
        [
          (<tx>balance[player1] >= balance[player1] + 2) || 
          (<tx>balance[player2] >= balance[player2] + 2)
        ]
      ]
}

// (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
property oracle_exact_balance_nonliquid {
    Forall xa
      [
        block.number<deadline && balance==2 
          -> 
        Exists tx [1, oracle]
        [
          (<tx>balance[player1] >= balance[player1] + 2) || 
          (<tx>balance[player2] >= balance[player2] + 2)
        ]
      ]
}

// once the players have redeemed their bets, the contract is liquid, namely any participant can withdraw the whole contract balance
property liquidity_notliquid {
    Forall xa
      [
        state==2
          -> 
        Exists tx [1, xa]
        [
          <tx>balance == 0
        ]
      ]
}