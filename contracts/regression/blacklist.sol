contract Blacklist {

  // anyone can deposit	
  function receive() payable { 
    skip
  }

  function pay(int amount) {
    require (amount<=balance && msg.sender!=1);
    msg.sender.transfer(amount)
  }

}


rule P1_nonliquid {
  forall a : address .
  exists v : int .   
    << a : Blacklist . pay() $ v >>		
      balance[a] == old(balance[a]) + balance
}

/*
rule P2_liquid {
  forall a : address .
  a!=1 ->
  exists v : int .   
    << a : Blacklist . pay() $ v >>		
      balance[a] == old(balance[a]) + balance
}
*/

/*
// STRONG SAT (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
property liquidity1_nonliquid {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        <tx>balance[xa] == balance[xa] + balance
      ]
    ]
}

// STRONG UNSAT
property liquidity2_liquid {
    Forall xa
    [
      xa != 1
        ->
      Exists tx [1, xa]
      [
        <tx>balance[xa] == balance[xa] + balance
      ]
    ]
}
*/