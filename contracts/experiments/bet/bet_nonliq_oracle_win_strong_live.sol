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
    require(state==0); // JOIN
    require (msg.value==1);
    require (msg.sender != player1);
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
	require(state==1); // WIN-OR-TIMEOUT
   	require(block.number>=deadline);
    state = 2; // END
    player1!1;
	player2!1
  }
}

// if deadline has passed and player2 has not joined, then anyone can make player1 redeem the bet 
property  oracle_win_strong_live {
    Forall xa
      [
        st.block.number<st.deadline && st.state==1 && st.balance >=2 
          -> 
        Exists tx [1, oracle]
        [
          ((app_tx_st.balance[player1] - st.balance[player1] >= 2) || (app_tx_st.balance[player2] - st.balance[player2] >= 2))
        ]
      ]
}

// if deadline_win has passed and the oracle has not chosen the winner, then anyone can make the players redeem their bets
