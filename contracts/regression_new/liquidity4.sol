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
rule P1_false {
  forall addr : address .
  exists v : int .   
    << addr : C4 . pay(v) $ 0 >>		
      balance[addr] == old(balance[addr]) + 1
}

rule P2_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ 0 >>
      balance[addr] == old(balance[addr]) + 1
}


rule P3_false {
  forall addr : address .
  exists v : int .   
    << addr : C4 . pay(v) $ 0 >>		
      balance[addr] == old(balance[addr]) + (balance - 1)
}

rule P4_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ 0 >>
      balance[addr] == old(balance[addr]) + (old(balance) - 1)
}


rule P5_false {
  forall addr : address .
  exists v : int .   
  << addr : C4 . pay(v) $ 0 >>
    balance[addr] == old(balance[addr]) + (old(balance) - 1)
}


// properties P6 and P7 are the same as P4 and P5 except for the "-1" inside/outside the scope of old()  
rule P6_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ 0 >>
      balance[addr] == old(balance[addr]) + old(balance - 1)
}


rule P7_false {
  forall addr : address .
  exists v : int .   
  << addr : C4 . pay(v) $ 0 >>
    balance[addr] == old(balance[addr]) + old(balance - 1)
}


rule P8_true {
  forall addr : address .
  exists v : int .   
  << addr : C4 . pay(v) $ 0 >>
    balance[addr] == old(balance[addr]) + old(balance) - balance
}


rule P9_false {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ 0 >>
      balance[addr] == old(balance[addr]) + (balance - 1) // note: we are using current balance 
}

*/

rule P10_true {
  forall addr : address .
  exists v : int .   
  << addr : C4 . pay(v) $ 0 >>
    !lastReverted ->
    balance[addr] == old(balance[addr]) + old(balance) - 1 
}


rule P11_false {
  forall addr : address .
  exists v : int .   
  << addr : C4 . pay(v) $ 0 >>
    lastReverted &&
    balance[addr] == old(balance[addr]) + old(balance) - 1
}


rule P12_true {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ 0 >>
      balance[addr] == old(balance[addr]) + old(balance) - 1
}

rule P13_false {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ 2 >>
      balance[addr] == old(balance[addr]) + old(balance) - 1
}

rule P14_true {
  forall addr : address .
  exists v : int .   
  exists xn : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ xn >>
      balance[addr] == old(balance[addr]) + old(balance) - 1
}

rule P15_false {
  forall addr : address .
  exists v : int .   
  st.balance > 1 ->		
    << addr : C4 . pay(v) $ v >>
      balance[addr] == old(balance[addr]) + old(balance) - 1
}

