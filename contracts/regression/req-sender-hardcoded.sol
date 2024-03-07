/// @custom:version liquidity3

contract C {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance && msg.sender==0);
    msg.sender!amount
  }
}


/// @custom:ground_truth false
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

// @custom:ground_truth true
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