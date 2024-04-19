/// @custom:version compliant with the specification.

contract Bet {
  const address oracle
  const address player1
  const int deadline

  address player2
  int state // 0 = JOIN, 1 = WIN-OR-TIMEOUT, 2 = END
  
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
    winner!balance
  }

  function timeout() {
    require(state==0 || state==1);
   	require(block.number>=deadline);
	  player1!1;
	  if (state==1) { player2!1 };
    state = 2 // END
  }
}

// if deadline_join has passed and player2 has not joined, then anyone can make player1 redeem the bet 
property  any_timeout_join_live {
    Forall xa
      [
        st.block.number>=st.deadline && st.state==0 
          -> 
        Exists tx [1, xa]
        [
          (app_tx_st.balance[player1] - st.balance[player1] >= 1)
        ]
      ]
}

// once player2 has joiuned and before the deadline, the oracle can transfer the bet to one of the players
// WEAK UNSAT