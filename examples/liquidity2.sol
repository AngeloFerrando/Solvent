contract C2 {
  address oracle
  
  constructor () {
    oracle=msg.sender
  }

  function pay(amount) {
    require (amount<=balance);
    msg.sender!amount
  }
  
}

// liquid
property liquidity2a_liq {
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
