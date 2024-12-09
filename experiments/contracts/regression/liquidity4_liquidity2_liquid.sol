contract C4 {
  
  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=(balance - 1));
    payable(sender).transfer(amount)
  }
}

// (WEAK SAT - WEAK UNSAT)
// Can_Transactions_Arrive_Any_time=True: STRONG SAT
// not liquid
property  liquidity2_liquid {
    Forall xa
    [
      st.balance > 1
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == st.balance[xa]  + (st.balance - 1)))
      ]
    ]
}