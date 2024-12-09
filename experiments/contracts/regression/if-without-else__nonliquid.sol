contract IfWithoutElse {

  constructor() payable {
    require(msg.value>0)
  }

  function pay() {
    if (false) {
        sender.transfer(1)
    }
  }
}


// not liquid
property  _nonliquid {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] > balance[xa]))
      ]
    ]
}