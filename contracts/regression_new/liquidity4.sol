contract C4 {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=(balance - 1));
    payable(sender).transfer(amount)
  }
}

/*
rule P0_false {
  forall addr : address .
  exists v : int .   
    << addr : C4 . pay() $ v >>		
      balance[addr] == old(balance[addr]) + 1
}

rule P1_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay() $ v >>
      balance[addr] == old(balance[addr]) + 1
}
*/

rule P2_false {
  forall addr : address .
  exists v : int .   
    << addr : C4 . pay() $ v >>		
      balance[addr] == old(balance[addr]) + (balance - 1)
}

rule P3_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay() $ v >>
      balance[addr] == old(balance[addr]) + (old(balance) - 1)
}

rule P4_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay() $ v >>
      balance[addr] == old(balance[addr]) + old(balance - 1)
}

rule P5_false {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay() $ v >>
      balance[addr] == old(balance[addr]) + (balance - 1) /* note: we are using current balance */
}


