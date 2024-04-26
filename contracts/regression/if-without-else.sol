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
property _nonlive {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > balance[xa]))
      ]
    ]
}