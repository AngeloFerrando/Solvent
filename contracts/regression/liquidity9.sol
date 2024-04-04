contract C9 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance && msg.sender!=1);
    msg.sender!amount
  }

}

// STRONG SAT
// (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
// not liquid
property liquidity9a_nonliq {
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


// STRONG UNSAT
// liquid
property liquidity9b_liq {
    Forall xa
    [
      xa != 1
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance ))
      ]
    ]
}