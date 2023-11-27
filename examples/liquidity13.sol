contract C13 {
  bool b

  constructor () {
    b = False;
    skip
  }

  function pay(amount) {
    require (amount <= balance && not b);
    msg.sender ! amount
  }

  function lock() {
    require(msg.sender == 0);
    b = true
  }

}
