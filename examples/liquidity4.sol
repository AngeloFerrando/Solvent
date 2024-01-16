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
      [balance>1 -> Exists s (s, xa) can_withdraw(balance - 1)]
}
