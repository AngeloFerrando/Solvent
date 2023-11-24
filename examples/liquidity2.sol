contract C2 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance);
    msg.sender!amount
  }
  
}
