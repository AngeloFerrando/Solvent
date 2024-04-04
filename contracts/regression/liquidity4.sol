contract C4 {

  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=(balance - 1));
    sender!amount
  }
}

// (WEAK SAT - WEAK UNSAT)
// Can_Transactions_Arrive_Any_time=True: STRONG SAT
// not liquid
property liquidity4a_nonliq {
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
property liquidity4b_liq {
    Forall xa
    [
      st.balance > 1
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + (st.balance - 1)))
      ]
    ]
}