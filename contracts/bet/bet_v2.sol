/// @custom:version uses token balances (unreliable!) to infer contract state.

contract Bet {

  address oracle
  int deadline
  address par1
  address par2

  constructor(o d) payable {
    require (msg.value==1);
    par1 = msg.sender;
    oracle = o;
    deadline = d
  }

  function join() payable {
    require(balance==1); 
    require (msg.value==1);
	require (msg.sender != par1);
    par2 = msg.sender
  }

  function win(winner) {
	require(balance==2);
	require(msg.sender==oracle);
    require(block.number<deadline);
	require(winner==par1 || winner==par2);
    winner!balance
  }

  function timeout() {
	  require(balance==2);
   	require(block.number>=deadline);
	  par1!1;
	  par2!1
  }

}
