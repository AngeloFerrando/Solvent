/// @custom:version compliant with the specification.

contract Bet {

  const address oracle
  const int deadline
  const address par1
  address par2
  int state // 0: join, 1: win-or-timeout, 2: end
   
  constructor(address o, int d) payable {
    require (msg.value==1);
    par1 = msg.sender;
    oracle = o;
    deadline = d;
    state = 0  
  }

  function join() payable {
    require(state==0);
    state = 1; 
    require (msg.value==1);
	  require (msg.sender != par1);
    par2 = msg.sender
  }

  function win(address winner) {
	  require(state==1);
    state = 2;
	  require(msg.sender==oracle);
    require(block.number<deadline);
	  require(winner==par1 || winner==par2);
    winner!balance
  }

  function timeout() {
	  require(state==1);
    state = 2;
   	require(block.number>=deadline);
	  par1!1;
	  par2!1
  }

}

// WEAK SAT WEAK UNSAT
property live2 {
    Forall xa
      [
        st.block.number<st.deadline && st.state == 1 
          -> 
        Exists tx [5, oracle]
        [
          ((app_tx_st.balance[par1] - st.balance[par1] >= 2) || (app_tx_st.balance[par2] - st.balance[par2] >= 2))
        ]
      ]
}
