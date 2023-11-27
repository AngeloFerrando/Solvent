contract C9 {

  constructor () {
    skip
  }

  function pay(amount) {
    require (amount<=balance && msg.sender!=0);
    msg.sender!amount
  }

}
