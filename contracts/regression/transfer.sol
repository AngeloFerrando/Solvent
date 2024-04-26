contract Transfer {
  address immutable rcv;

  constructor() payable {
    rcv = msg.sender
  }
  function withdraw(int v) {
    require(v<=balance);
    rcv.transfer(v)
  }
}

property liquidity_live {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[st.rcv] == balance[st.rcv] + balance
      ]
    ]
}
