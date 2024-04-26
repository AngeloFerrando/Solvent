contract C {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=balance);
    msg.sender.transfer(amount)
  }
  
}

// liquid
property liquidity2a_live {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == balance[xa] + balance
      ]
    ]
}
