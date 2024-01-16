contract C3 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance && msg.sender==0);
    msg.sender!amount
  }
}

property {
  Forall xa  
      [xa==0 -> Exists s (s, xa) can_withdraw(balance)]
}
