contract Constructor1 {

  constructor() payable {
    require(msg.value==0)
  }

  function pay(int amount) {
    msg.sender.transfer(1)
  }
}


// liquid
property liquidity1_nonlive {
    Forall xa
    [
        true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}