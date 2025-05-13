contract IfNested1 {
  int val;
  address pippo;

  constructor() payable {
    require(msg.value>0);
    val = 0
  }

  function pay(int n) {
    if (n>5) {
        val = val+1 
    } else {
        if (n<5) {
            skip
        }
        else {
            //require(val>=1);
            if (val>=1) {
              sender.transfer(1)
            }
        }
    }
  }
}

property tx1_nonliquid {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [1, xa]
      [
        ((<tx>balance[pippo] > balance[xa] && <tx>val >= 1))
      ]
    ]
}

property tx2_liquid {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [2, xa]
      [
        ((<tx>balance[xa] > balance[xa] && <tx>val >= 1))
      ]
    ]
}