contract Sender {
  // sender is taken as a name, so a different one has to be used
  address sender_field

  function receive() payable { skip }

  // error: it should be msg.sender
  function pay() { sender.transfer(balance) }
}

property  pay_liquid {
    Forall xa
    [
      st.balance>0
        ->
      Exists tx [1, xa]
      [
        (<tx>balance[xa] > balance[xa])
      ]
    ]
}
