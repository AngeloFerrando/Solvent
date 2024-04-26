contract C14 {
  bool b;

  constructor () {
    b = false
  }

  function unlock() {
    require(!b); 
    b = true
  }

  function pay(int amount) {
    require (amount <= balance && b);
    b = false;
    sender.transfer(amount)
  }

}

property liquidity1_notlive {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa] + balance))
      ]
    ]
}

property liquidity2_live {
    Forall xa
    [
      st.b == true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa] + balance))
      ]
    ]
}

property liquidity3_live {
    Forall xa
    [
      true
        ->
      Exists tx [2, xa]
      [
        ((<tx>balance[xa] == balance[xa] + balance ))
      ]
    ]
}

