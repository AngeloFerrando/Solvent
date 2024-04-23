contract Conter {
  address immutable owner
  int immutable maxCount
  int count

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
        msg.sender!balance 
    }
  }
}

property liquidity1_live {
    Forall xa
    [
      st.balance>0 && st.count<st.maxCount && st.owner!=xa
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}

property liquidity2_notlive {
    Forall xa
    [
      st.balance>0 && st.count<st.maxCount
        ->
      Exists tx [2, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}

property liquidity3_notlive {
    Forall xa
    [
      st.balance>0 && st.owner!=xa
        ->
      Exists tx [2, xa]
      [
        app_tx_st.balance[xa] == st.balance[xa] + st.balance
      ]
    ]
}