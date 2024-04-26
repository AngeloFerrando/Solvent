contract Blacklist {

  // anyone can deposit	
  function receive() payable { 
    skip
  }

  function pay(int amount) {
    require (amount<=balance && msg.sender!=1);
    msg.sender.transfer(amount)
  }

}

// STRONG SAT (Can_Transactions_Arrive_Any_time=False WEAK SAT WEAK UNSAT)
property liquidity1_nonlive {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}

// STRONG UNSAT
property liquidity2_live {
    Forall xa
    [
      xa != 1
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}