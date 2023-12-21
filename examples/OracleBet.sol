contract OracleBet {
  address p1
  address p2

  constructor(p) {
      p1 = msg.sender;
      p2 = p
  } 

  function deposit() payable {
      require (msg.sender==p2 && msg.value==1);
      skip
  }
  
  function pay() {
    require (msg.sender==p1);
    msg.sender!(balance) 
  }
}
