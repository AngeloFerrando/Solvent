
contract AMM {
	mapping (address => int) bal0;
	mapping (address => int) bal1;
    bool tout;
    int yout;

	constructor(int x0, int x1) {
        require(x0 > 0 && x1 > 0);
        bal0[msg.sender] = bal0[msg.sender] - x0;
        bal1[msg.sender] = bal1[msg.sender] - x1;  
        bal0[this] = x0;
        bal1[this] = x1
    }

    /* tin is 0 if T0; 1 if T1 */
	function swap(int xin, bool tin, int ymin) {
		require(xin > 0);
		tout = not tin;
		if (tout) {
        yout = xin * (bal1[this] / bal0[this]);
        require (yout >= ymin && yout<bal1[this]);
        bal0[this] = bal0[this] + xin;
        bal0[msg.sender] = bal0[msg.sender] - xin;
        bal1[this] = bal1[this] - yout;
        bal1[msg.sender] = bal1[msg.sender] + yout
      }
		else {
        yout = xin * bal0[this] / bal1[this];
        require (yout >= ymin && yout<bal0[this]);
        bal1[this] = bal1[this] + xin;
        bal1[msg.sender] = bal1[msg.sender] - xin;
        bal0[this] = bal0[this] - yout;
        bal0[msg.sender] = bal0[msg.sender] + yout
      }
	}
}


rule Test {
  forall a : address .  
    << a : AMM . swap(0 , False , 0) $ 0 >>		
      true
}



rule P1_false {
  forall a : address .  
    << a : AMM . swap(0 , False , 0) $ 0 >>		
      bal0[this] > old(bal0[this])
}

rule P2_true {
  forall a : address .  
    << a : AMM . swap(1 , False , 0) $ 0 >>		
      bal0[this] > old(bal0[this])
}


rule P3_false {
  forall a : address .  
    << a : AMM . swap(0 , False , 0) $ 0 >>		
      bal1[this] < old(bal1[this])
}

rule P4_true {
  forall a : address .  
    << a : AMM . swap(1 , False , 0) $ 0 >>		
      bal1[this] < old(bal1[this])
}

