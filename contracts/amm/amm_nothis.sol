
contract AMM {
	mapping (address => int) bal0;
	mapping (address => int) bal1;
  int bal0_AMM;
  int bal1_AMM;
    bool tout;
    int yout;

	constructor(int x0, int x1) {
        require(x0 > 0 && x1 > 0);
        bal0[msg.sender] = bal0[msg.sender] - x0;
        bal1[msg.sender] = bal1[msg.sender] - x1;  
        bal0_AMM = x0;
        bal1_AMM = x1
    }

    /* tin is 0 if T0; 1 if T1 */
	function swap(int xin, bool tin, int ymin) {
    require(bal0_AMM > 0 && bal1_AMM > 0);
		require(xin > 0);
		tout = not tin;
		if (tout) {
        yout = xin * (bal1_AMM / bal0_AMM);
        require (yout >= ymin && yout<bal1_AMM);
        bal0_AMM = bal0_AMM + xin;
        bal0[msg.sender] = bal0[msg.sender] - xin;
        bal1_AMM = bal1_AMM - yout;
        bal1[msg.sender] = bal1[msg.sender] + yout
      }
		else {
        yout = xin * bal0_AMM / bal1_AMM;
        require (yout >= ymin && yout<bal0_AMM);
        bal1_AMM = bal1_AMM + xin;
        bal1[msg.sender] = bal1[msg.sender] - xin;
        bal0_AMM = bal0_AMM - yout;
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
      bal0_AMM > old(bal0_AMM)
}

rule P2_true {
  forall a : address .  
    << a : AMM . swap(1 , False , 0) $ 0 >>		
      bal0_AMM > old(bal0_AMM)
}


rule P3_false {
  forall a : address .  
    << a : AMM . swap(0 , False , 0) $ 0 >>		
      bal1_AMM < old(bal1_AMM)
}

rule P4_true {
  forall a : address .  
    << a : AMM . swap(1 , False , 0) $ 0 >>		
      bal1_AMM < old(bal1_AMM)
}

