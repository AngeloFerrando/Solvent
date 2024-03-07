contract C11 {
  
  constructor () {
    skip
  }
  function pay(amount) {
    require (amount <= balance);
    if (msg.sender == 0) {
      msg.sender ! amount - 1
    }
    else {
      msg.sender ! amount
    }
  }

}


// not liquid
property liquidity11a_nonliq {
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


/*
// liquid
property liquidity11b_liq {
    Forall xa
    [
      xa != 0
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance ))
      ]
    ]
}
*/