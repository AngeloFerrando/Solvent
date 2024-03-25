contract IfNested1 {

  constructor() payable {
    require(msg.value>0)
  }

  function pay(n) {
    if (n>5) {
        skip
    } else {
        if (n<5) {
            skip
        }
        else {
            sender!1
        }
    }
  }
}


// not liquid
property notliq {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}