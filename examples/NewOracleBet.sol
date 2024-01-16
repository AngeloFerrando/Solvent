contract OracleBet {

  address oracle
  int deadline
  address p1
  address p2

  constructor(o d) payable {
    require (msg.value==1);
    p1 = msg.sender;
    oracle = o;
    deadline = d
  }

  function join() payable {
    require(balance==1); 
    require (msg.value==1);
	require (msg.sender != p1);
    p2 = msg.sender
  }

  function win(winner) {
	require(balance==2);
	require(msg.sender==oracle);
    require(block.number<deadline);
	require(winner==p1 || winner==p2);
    winner!balance
  }

  function timeout() {
	require(balance==2);
   	require(block.number>=deadline);
	p1!1;
	p2!1
  }

}

property {
    Forall xa  
      [block.number<deadline && balance==2 -> Exists s (s, oracle) can_withdraw(p1,2) || can_withdraw(p2,2)]
}

//property {
//	forall xa  
//	    [block.number>timeout && balance==2 -> Exists s (s, xa) (can_withdraw(p1,1) && can_withdraw(p2,1))]
//}