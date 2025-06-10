contract C4 {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=(balance - 1));
    payable(sender).transfer(amount)
  }
}

rule Liquidity1_nonliquid {
  forall a : address .
  exists v : int .   
    << a : C4 . pay() $ v >>		
      balance[a] == old(balance[a]) + 1
}