contract C15 {
  address immutable owner;

  constructor () {
    owner = msg.sender
  }

  function pay(int amount) {
    require (amount <= balance);
    //owner ! amount
    if (owner == msg.sender) {
      msg.sender.transfer(amount)
    } 
    else {
      skip
    }
  }

} 

// STRONG SAT (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
property  liquidity15a_nonliquid {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa]  + balance))
      ]
    ]
}