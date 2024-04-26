contract C4 {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=(balance - 1));
    sender.transfer(amount)
  }
}

// (WEAK SAT - WEAK UNSAT)
// Can_Transactions_Arrive_Any_time=True: STRONG SAT
// not liquid
property liquidity1_nonlive {
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
property liquidity2_live {
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