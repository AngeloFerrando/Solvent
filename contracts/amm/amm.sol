
contract AMM {
    address immutable a0;
	mapping (address => int) bal0;
	mapping (address => int) bal1;
    bool tout;
    int yout;

	constructor(int x0, int x1) {
        require(x0 > 0 && x1 > 0);
        bal0[msg.sender] = bal0[msg.sender] - x0;
        bal1[msg.sender] = bal1[msg.sender] - x1;  
        bal0[a0] = x0;
        bal1[a0] = x1
    }

    /* tin is 0 if T0; 1 if T1 */
	function swap(int xin, bool tin, int ymin) {
		require(xin > 0);
		tout = not tin;
		if (tout) {
            yout = xin * (bal1[a0] / bal0[a0]);
			require (yout >= ymin && yout<bal1[a0]);
			bal1[a0] = bal1[a0] - yout;
			bal1[msg.sender] = bal1[msg.sender] + yout
        }
		else {
            yout = xin * bal0[a0] / bal1[a0];
			require (yout >= ymin && yout<bal0[a0]);
			bal0[a0] = bal0[a0] - yout;
			bal0[msg.sender] = bal0[msg.sender] + yout
        }
	}
}



rule Dummy1 {
    True
}

/*
rule Dummy {
  forall a : address .  
    << a : AMM . swap(0 , False , 0) $ 0 >>		
      bal0[a] == old(bal0[a]) + 1
}*/