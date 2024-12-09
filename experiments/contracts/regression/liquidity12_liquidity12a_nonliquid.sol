contract C12 {

  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount <= balance);
    if (msg.sender != 1) {
      msg.sender.transfer(amount - 1)
    }
    else {
      msg.sender.transfer(amount)
    }
  }

}

// STRONG SAT
// (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
// not liquid
property  liquidity12a_nonliquid {
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


// STRONG SAT
// (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
// not  liquid
