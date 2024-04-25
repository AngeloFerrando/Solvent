// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Freezable {
    address owner;
    bool frozen;
    
    constructor () payable {
	owner = msg.sender;
    }

    function freeze(bool f) external {
	require (msg.sender == owner);
	frozen = f;
    }

    function withdraw(uint amount) external {
        // require(amount <= address(this).balance);
	    require(!frozen);
	    // require(amount!=42); // just to check if amount in the rule is quantifies universally or existentially
        payable(msg.sender).transfer(amount);
    }

    function getBal(address a) public view returns (uint) {
	return a.balance;
    }
}
