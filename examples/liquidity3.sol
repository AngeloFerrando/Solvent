contract C3 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance && msg.sender==0);
    msg.sender!amount
  }
}


// not liquid
property liquidity3a_nonliq {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}

// liquid
property liquidity3b_liq {
    Forall xa
    [
      xa == 0
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}