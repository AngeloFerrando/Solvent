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

property  liquidity2_liquid {
    Forall xa
    [
      st.balance>0 && xa==0
        ->
      Exists tx [1, xa]
      [
        <tx>balance[xa] == balance[xa] + balance
      ]
    ]
}