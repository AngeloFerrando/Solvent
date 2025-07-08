contract C4 {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=(balance - 1));
    payable(sender).transfer(amount)
  }
}

rule Liquidity4_nonliquid {
  forall addr : address .
  exists v : int .   
    << addr : C4 . pay() $ v >>		
      balance[addr] == old(balance[addr]) + 1
}


rule Liquidity4_liquid {
  forall addr : address .
  exists v : int .   
    << addr : C4 . pay() $ v >>
      st.balance > 1 ->		
      balance[addr] == old(balance[addr]) + (st.balance - 1)
}
