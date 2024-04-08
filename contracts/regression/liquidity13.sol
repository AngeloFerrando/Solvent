contract C13 {
  bool b

  constructor () {
    b = False;
    skip
  }

  function pay(int amount) {
    require (amount <= balance && not b);
    msg.sender ! amount
  }

  function lock() {
    require(msg.sender == 1);
    b = true
  }

}


// not liquid
property liquidity13a_nonlive {
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
property liquidity13b_live {
    Forall xa
    [
      st.b == false
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}