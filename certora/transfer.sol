// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Transfer {
    address payable immutable rcv;

    constructor() payable {
        rcv = payable(msg.sender);
    }

    function withdraw(uint v) public {
        require(v<=address(this).balance);
	    rcv.transfer(v);
    }

    function getBal(address a) public view returns(uint) {
    	return a.balance;
    }

    function invariant(uint v) public {
        uint s0 = rcv.balance;
        uint c0 = address(this).balance;

        withdraw(v);

        uint s1 = rcv.balance;
        uint c1 = address(this).balance;
        
        assert(s1==s0+v && c1==c0-v);
    }
}
