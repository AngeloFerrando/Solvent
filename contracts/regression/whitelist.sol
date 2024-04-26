contract Whitelist {

  // anyone can deposit	
  function receive() payable { 
	skip
  }

  function pay(int amount) {
    require (amount<=balance && msg.sender==0);
    msg.sender.transfer(amount)
  }
}

property liquidity1_notlive {
    Forall xa
    [
      st.balance>0
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}

property liquidity2_live {
    Forall xa
    [
      st.balance>0 && xa==0
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}