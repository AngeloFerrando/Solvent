contract C15 {
  bool b

  constructor () {
    b = False;
    skip
  }

  function unlock() {
    require(not b); 
    b = true
  }

  function pay(amount) {
    require (amount <= balance && b);
    b = false;
    sender ! amount
  }

}
