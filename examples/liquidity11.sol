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

property {
    Forall xa
    [
      xa == 0
        ->
      Exists tx [2, xa]
      [
        tx.msg.sender==st.xa && ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}

