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

property {
    Forall xa
    [
      true
        ->
      Exists tx [3, oracle]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}
