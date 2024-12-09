contract C11 {
  
  constructor () {
    skip
  }
  
  function pay(int amount) {
    require (amount <= balance);
    if (msg.sender == 1) {
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
property  liquidity11b_liq {
    Forall xa
    [
      xa != 1
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == st.balance[xa]  + st.balance ))
      ]
    ]
}

