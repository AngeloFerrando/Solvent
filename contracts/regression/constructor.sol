contract Constructor1 {

  constructor() payable {
    require(msg.value==0)
  }

  function pay(amount) {
    sender!1
  }
}


// liquid
property liquidity1_liq {
    Forall xa
    [
        true
        ->
      Exists tx [5, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}