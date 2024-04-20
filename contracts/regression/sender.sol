contract Sender {
  address sender

  function receive() payable { skip }

  // error: it should be msg.sender
  function pay() { sender!balance }
}

property pay_nonlive {
    Forall xa
    [
      st.balance>0
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance[xa] > st.balance[xa])
      ]
    ]
}
