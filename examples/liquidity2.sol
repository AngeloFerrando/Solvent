contract C2 {
  address oracle
  //(address -> int) m
  
  constructor () {
    oracle=msg.sender//;
    //m[msg.sender] = 1
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
