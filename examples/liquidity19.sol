contract C19 {

  constructor () {
    skip
  }

  function pay(receiver, amount) {
    require (amount<=balance);
    receiver!amount
  }
  
}

property {
  Forall xa, xb  
      [true -> Exists s (s, xa) can_withdraw(xb, balance)]
}
