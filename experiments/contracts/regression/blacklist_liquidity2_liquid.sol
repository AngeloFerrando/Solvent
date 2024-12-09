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

// STRONG SAT (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
property  liquidity2_liquid {
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