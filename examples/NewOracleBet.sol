contract OracleBet {

  address oracle
  int deadline
  address par1
  address par2

  constructor(o d) payable {
    require (msg.value==1);
    par1 = msg.sender;
    oracle = o;
    deadline = d
  }

  function join() payable {
    require(balance==1); 
    require (msg.value==1);
	  require (msg.sender != par1);
    par2 = msg.sender
  }

  function win(winner) {
	  require(balance==2);
	  require(msg.sender==oracle);
    require(block.number<deadline);
	  require(winner==par1 || winner==par2);
    winner!balance
  }

  function timeout() {
	  require(balance==2);
   	require(block.number>=deadline);
	  par1!1;
	  par2!1
  }

}

property liq1 {
    Forall xa
      [
        st.block.number<st.deadline && st.balance==2 
          -> 
        Exists tx [5, oracle]
        [
          ((app_tx_st.balance[par1] - st.balance[par1] >= 2) || (app_tx_st.balance[par2] - st.balance[par2] >= 2))
        ]
      ]
}

/*
property {
    Forall xa  
      [block.number<deadline && balance==2 -> Exists s (s, xa) xa==oracle && can_withdraw(s,par1,2) || can_withdraw(s,par2,2)]
}

property {
    Forall xa  
      [block.number<deadline && balance==2 -> Exists tx . tx.msg.sender==oracle && can_withdraw(tx,par1,2) || can_withdraw(tx,par2,2)]
}


property {
  Forall st (implicito: stato reachable del contratto)
    Forall xa (non usato in questo esempio, ma in altri sì, ad es. Bank)
      [st.block.number<st.deadline && st.balance==2 -> Exists tx . tx.fun==win && tx.msg.sender==st.oracle && (((app tx st).balance(par1) - st.balance(par1) >= 2) || ((app tx st).balance(par2) - st.balance(par1) >= 2))]
}

property {
  Forall st (implicito: stato reachable del contratto)
    Forall xa (non usato in questo esempio, ma in altri sì, ad es. Bank)
      [st.block.number<st.deadline && st.balance==2 -> Exists tx . tx = oracle:win(par1) && tx.msg.sender==st.oracle && (((app tx st).balance(par1) - st.balance(par1) >= 2) || ((app tx st).balance(par2) - st.balance(par1) >= 2))]
}*/

//property {
//	forall xa  
//	    [block.number>timeout && balance==2 -> Exists s (s, xa) (can_withdraw(par1,1) && can_withdraw(par2,1))]
//}