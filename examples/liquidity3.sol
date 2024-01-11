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
    Exists s (s, xa) 
      [xa==0 -> can_withdraw(balance)]
}
