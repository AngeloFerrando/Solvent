contract C {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=balance);
    msg.sender.transfer(amount)
  }
  
}

// liquid
property  liquidity2a_liquid {
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
