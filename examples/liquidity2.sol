contract C2 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance);
    msg.sender!amount
  }
  
}

property {
  Forall xa  
      [true -> Exists s (s, xa) can_withdraw(balance)]
}
