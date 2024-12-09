contract IfWithoutElse2 {
  bool success;

  constructor() payable {
    require(msg.value>0)
  }

  function foo() payable {
    if (balance >= 10) {
        success = true
    } else { skip }
  }
}

property  _liquid {
    Forall xa
    [
      balance>0
      ->
      Exists tx [1, xa]
      [
        ((<tx>success))
      ]
    ]
}