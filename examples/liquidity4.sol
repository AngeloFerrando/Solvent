contract C4 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=(balance - 1));
    sender!amount
  }
}

property {
  Forall xa 
    Exists s (s, xa) 
      [balance>1 -> can_withdraw(balance - 1)]
}
