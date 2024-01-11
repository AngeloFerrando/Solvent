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
    Exists s (s, xa) 
      [true -> can_withdraw(balance)]
}
