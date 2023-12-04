contract C15 {
  address owner

  constructor () {
    owner = msg.sender
  }

  function pay(amount) {
    require (amount <= balance);
    //owner ! amount
    if (owner == msg.sender) {
      msg.sender ! amount
    } else {
      skip
    }
  }

} 
