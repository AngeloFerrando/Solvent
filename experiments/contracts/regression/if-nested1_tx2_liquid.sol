contract IfNested1 {
  int x;

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
            //require(x>=1);
            if (x>=1) {
              sender.transfer(1)
            }
        }
    }
  }
}

property  tx2_liquid {
    Forall xa
    [
      st.balance>0
      ->
      Exists tx [2, xa]
      [
        ((<tx>balance[xa] > balance[xa] && <tx>x >= 1))
      ]
    ]
}