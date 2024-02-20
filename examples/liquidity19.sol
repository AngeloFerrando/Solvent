contract C19 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance);
    msg.sender!amount
  }
  
}

// liquid
property liquidity19a_liq {
    Forall xa
    [
      true
        ->
      Exists tx [5, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}
