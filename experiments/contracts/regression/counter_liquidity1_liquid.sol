contract Counter {
  address immutable owner;
  int immutable maxCount;
  int count;

  constructor() payable {
    require(msg.value>0);
    owner = msg.sender;
    maxCount = 3;
    count = 0
  } 
  
  function pay() {
    require (count<maxCount);
    if (msg.sender==owner) { 
        count=count+1 
    }
    else { 
        count = count;
        msg.sender.transfer(balance) 
    }
  }
}

property  liquidity1_liquid {
    Forall xa
    [
      st.balance>0 && st.count<st.maxCount && st.owner!=xa
        ->
      Exists tx [1, xa]
      [
        <tx>balance[xa] == balance[xa] + balance
      ]
    ]
}

