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
property  liquidity1_nonliquid {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa]  + balance))
      ]
    ]
}

// STRONG UNSAT
// liquid
