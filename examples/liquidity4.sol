contract C4 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=(balance - 1));
    sender!amount
  }
}
