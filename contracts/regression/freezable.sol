contract Freezable {
  address immutable owner;
  bool frozen;

  constructor () payable {
    owner = msg.sender
  }
  
  function freeze() {
    require (msg.sender == owner);
    frozen = true
  }

  function pay(int v) {
    require (!frozen);
    msg.sender.transfer(v)
  }
}

property liquidity1_nonlive {
    Forall xa
    [
      true
      ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == balance[xa] + balance
      ]
    ]
}

property liquidity2_live {
    Forall xa
    [
      !st.frozen
      ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[xa] == balance[xa] + balance
      ]
    ]
}