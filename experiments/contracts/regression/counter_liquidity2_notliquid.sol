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

property  liquidity2_notliquid {
    Forall xa
    [
      st.balance>0 && st.count<st.maxCount
        ->
      Exists tx [2, xa]
      [
        <tx>balance[xa] == balance[xa] + balance
      ]
    ]
}

