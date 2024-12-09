contract C19 {

  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=balance);
    msg.sender.transfer(amount)
  }
  
}

// STRONG UNSAT
property  liquidity19a_liquid {
    Forall xa
    [
      true
        ->
      Exists tx [5, xa]
      [
        ((<tx>balance[xa] == balance[xa]  + balance))
      ]
    ]
}
