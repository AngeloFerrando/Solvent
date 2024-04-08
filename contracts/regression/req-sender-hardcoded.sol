/// @custom:version liquidity3

contract C {

  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=balance && msg.sender==1);
    msg.sender!amount
  }
}


/// @custom:ground_truth false
property liquidity3a_nonlive {
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
property liquidity3b_live {
    Forall xa
    [
      xa == 1
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}