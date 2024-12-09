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

property  liquidity2_liquid {
    Forall xa
    [
      !st.frozen
      ->
      Exists tx [1, xa]
      [
        <tx>balance[xa] == balance[xa] + balance
      ]
    ]
}