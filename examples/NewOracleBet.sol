contract OracleBet {

  address oracle
  int deadline
  address p1
  address p2

  constructor(o d) payable {
    require (msg.value==1);
    p1 = msg.sender;
    oracle = o;
    deadline = d
  }

  function join() payable {
    require(balance==1); 
    require (msg.value==1);
	  require (msg.sender != p1);
    p2 = msg.sender
  }

  function win(winner) {
	  require(balance==2);
	  require(msg.sender==oracle);
    require(block.number<deadline);
	  require(winner==p1 || winner==p2);
    winner!balance
  }

  function timeout() {
	  require(balance==2);
   	require(block.number>=deadline);
	  p1!1;
	  p2!1
  }

}

property {
    Forall xa
      [
        st.block.number<st.deadline && st.balance==2 
          -> 
        Exists tx 
        [
          tx.msg.sender==st.oracle && ((app_tx_st.balance[p1] - st.balance[p1] >= 2) || (app_tx_st.balance[p2] - st.balance[p2] >= 2))
        ]
      ]
}

/*
property {
    Forall xa  
      [block.number<deadline && balance==2 -> Exists s (s, xa) xa==oracle && can_withdraw(s,p1,2) || can_withdraw(s,p2,2)]
}

property {
    Forall xa  
      [block.number<deadline && balance==2 -> Exists tx . tx.msg.sender==oracle && can_withdraw(tx,p1,2) || can_withdraw(tx,p2,2)]
}


property {
  Forall st (implicito: stato reachable del contratto)
    Forall xa (non usato in questo esempio, ma in altri sì, ad es. Bank)
      [st.block.number<st.deadline && st.balance==2 -> Exists tx . tx.fun==win && tx.msg.sender==st.oracle && (((app tx st).balance(p1) - st.balance(p1) >= 2) || ((app tx st).balance(p2) - st.balance(p1) >= 2))]
}

property {
  Forall st (implicito: stato reachable del contratto)
    Forall xa (non usato in questo esempio, ma in altri sì, ad es. Bank)
      [st.block.number<st.deadline && st.balance==2 -> Exists tx . tx = oracle:win(p1) && tx.msg.sender==st.oracle && (((app tx st).balance(p1) - st.balance(p1) >= 2) || ((app tx st).balance(p2) - st.balance(p1) >= 2))]
}*/

//property {
//	forall xa  
//	    [block.number>timeout && balance==2 -> Exists s (s, xa) (can_withdraw(p1,1) && can_withdraw(p2,1))]
//}