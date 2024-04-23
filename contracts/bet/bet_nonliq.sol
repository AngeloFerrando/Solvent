/// @custom:version compliant with the specification.

contract Bet {
  address immutable oracle
  address immutable player1
  int immutable deadline

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
property any_timeout_nonlive {
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
property oracle_win_live {
    Forall xa
      [
        st.block.number<st.deadline && st.state==1 
          -> 
        Exists tx [1, oracle]
        [
          ((app_tx_st.balance[player1] - st.balance[player1] >= 2) || (app_tx_st.balance[player2] - st.balance[player2] >= 2))
        ]
      ]
}

// in state WIN-OR-TIMEOUT and before `deadline`, the oracle can transfer the whole pot to one of the players
// STRONG UNSAT
property oracle_win_strong_live {
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
property any_timeout_win_live {
    Forall xa
      [
        st.block.number>=st.deadline && st.state==1 && st.balance >=2 
          -> 
        Exists tx [1, xa]
        [
          ((app_tx_st.balance[player1] - st.balance[player1] >= 1) && (app_tx_st.balance[player2] - st.balance[player2] >= 1))
        ]
      ]
}

// (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
property oracle_exact_balance_nonlive {
    Forall xa
      [
        st.block.number<st.deadline && st.balance==2 
          -> 
        Exists tx [1, oracle]
        [
          ((app_tx_st.balance[player1] - st.balance[player1] >= 2) || (app_tx_st.balance[player2] - st.balance[player2] >= 2))
        ]
      ]
}
