contract Constructor1 {

  constructor() payable {
    require(msg.value==0)
  }

  function pay(int amount) {
    msg.sender.transfer(1)
  }
}


// liquid
property  liquidity1_nonliquid {
    Forall xa
    [
        true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] > balance[xa]))
      ]
    ]
}