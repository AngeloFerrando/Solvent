// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract C1 {
    uint maxCount;
    uint count;
    address owner;

  constructor() payable {
    owner = msg.sender;
    maxCount = 10;
    count = 0;
  } 

  function inc() public {
    if (msg.sender==owner) { 
        count=count+1;
    }
  }
  
  function pay() public {
    require (count<maxCount);

    uint amount = address(this).balance;	
    (bool succ,) = msg.sender.call{value: amount}("");
    require(succ);	
  }

  function getBal(address a) public view returns(uint) {
      return address(a).balance;
  }
}

// certoraRun C1.sol --verify C1:C1.spec
// assert fails because of havoc on low-level call

contract C1b {
    uint maxCount;
    uint count;
    address owner;
    
    uint abal; // caller balance  
    uint cbal; // contract balance 
    
    constructor() payable {
	owner = msg.sender;
	maxCount = 10;
	count = 0;
	
	abal = 0;
	cbal = msg.value;
    } 
    
    function inc() public {
	if (msg.sender==owner) { 
	    count=count+1;
	}
    }
    
    function pay() public {
	require (count<maxCount);

	// needed to avoid that the assert is violated because of overflows
	if (cbal > 0) abal += cbal;
	cbal = 0;
    }
    
    function getBal(address a) public view returns(uint) {
	return abal;
    }
}

// certoraRun C1.sol:C1b --verify C1b:C1.spec
// assert fails because count==maxCount
// This is correct, since count can be incremented through inc (public)


// inc visibility changed to private

contract C1c {
    uint maxCount;
    uint count;
    address owner;
    
    uint abal; // caller balance  
    uint cbal; // contract balance 
    
    constructor() payable {
	owner = msg.sender;
	maxCount = 10;
	count = 0;
	
	abal = 0;
	cbal = msg.value;
    } 
    
    function inc() private {
	if (msg.sender==owner) { 
	    count=count+1;
	}
    }
    
    function pay() public {
	require (count<maxCount);

	// needed to avoid that the assert is violated because of overflows
	if (cbal > 0) abal += cbal;
	cbal = 0;
    }
    
    function getBal(address a) public view returns(uint) {
	return abal;
    }
}


// certoraRun C1.sol:C1c --verify C1c:C1.spec
// assert fails because count==maxCount
// This is NOT correct, since count cannot be incremented through inc (private)
