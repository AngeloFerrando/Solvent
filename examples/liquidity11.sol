contract C11 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount <= balance);
    if (msg.sender == 0) {
      msg.sender ! amount - 1
    }
    else {
      msg.sender ! amount
    }
  }

}
