contract C2 {

  constructor () {
    skip
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
      Exists tx
      [
        tx.msg.sender==st.xa && ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
    [5]
}
