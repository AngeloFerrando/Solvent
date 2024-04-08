contract IfNested1 {
  int x

  constructor() payable {
    require(msg.value>0);
    x = 0
  }

  function pay(int n) {
    if (n>5) {
        x = x+1 
    } else {
        if (n<5) {
            skip
        }
        else {
            require(x>=1);
            sender!1
        }
    }
  }
}

// not liquid
property _nonlive {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [2, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa] && app_tx_st.x >= 1))
      ]
    ]
}