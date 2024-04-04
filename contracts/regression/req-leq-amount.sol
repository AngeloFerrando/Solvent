/// @custom:version liquidity2

contract C {
  
  constructor () {
    skip
  }

  function pay(int amount) {
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
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}
