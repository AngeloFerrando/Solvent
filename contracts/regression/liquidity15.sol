contract C15 {
  address owner

  constructor () {
    owner = msg.sender
  }

  function pay(amount) {
    require (amount <= balance);
    //owner ! amount
    if (owner == msg.sender) {
      msg.sender ! amount
    } else {
      skip
    }
  }

} 

// not liquid
property liquidity15a_nonliq {
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