contract IfWithoutElse2 {

  bool success

  constructor() payable {
    require(msg.value>0)
  }

  function foo() payable {
    if (balance >= 10) {
        success = true
    } else { skip }
  }
}

property _live {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [1, xa]
      [
        ((app_tx_st.success))
      ]
    ]
}