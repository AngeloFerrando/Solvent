
contract AMM {
  int counter;
  int bal0_AMM; 
  int bal1_AMM;
  int bal0_def;
  int bal1_def;
  int bal0_att;
  int bal1_att;
    bool tout;
    int yout;

	constructor(int x0, int x1) {
        //require(x0 > 0 && x1 > 0);
        counter = 0;
        bal0_AMM = 60;
        bal1_AMM = 40;
        bal0_def = 10;
        bal1_def = 20;
        bal0_att = 100;
        bal1_att = 100
    }

    /* tin is 0 if T0; 1 if T1 */
	function swap_def(int xin, bool tin, int ymin) {
    require(bal0_AMM > 0 && bal1_AMM > 0);
		require(xin > 0);
		tout = not tin;
    counter = counter + 1;
		if (tout) {
        yout = xin * (bal1_AMM / (bal0_AMM + xin));
        //yout = 15;
        require (yout >= ymin && yout<bal1_AMM);
        bal0_AMM = bal0_AMM + xin;
        bal0_def = bal0_def - xin;
        bal1_AMM = bal1_AMM - yout;
        bal1_def = bal1_def + yout
      }
		else {
        yout = xin * bal0_AMM / (bal1_AMM + xin);
        //yout = 15;
        require (yout >= ymin && yout<bal0_AMM);
        bal1_AMM = bal1_AMM + xin;
        bal1_def = bal1_def - xin;
        bal0_AMM = bal0_AMM - yout;
        bal0_def = bal0_def + yout
      }
	}


    /* tin_att is 0 if T0; 1 if T1 */
	function swap_att(int xin_att, bool tin_att, int ymin_att) {
    require(bal0_AMM > 0 && bal1_AMM > 0);
		require(xin_att > 0);
		tout = not tin_att;
    counter = counter + 1;
		if (tout) {
        yout = xin_att * (bal1_AMM / (bal0_AMM + xin_att));
        require (yout >= ymin_att && yout<bal1_AMM);
        bal0_AMM = bal0_AMM + xin_att;
        bal0_att = bal0_att - xin_att;
        bal1_AMM = bal1_AMM - yout;
        bal1_att = bal1_att + yout
      }
		else {
        yout = xin_att * bal0_AMM / (bal1_AMM + xin_att);
        require (yout >= ymin_att && yout<bal0_AMM);
        bal1_AMM = bal1_AMM + xin_att;
        bal1_att = bal1_att - xin_att;
        bal0_AMM = bal0_AMM - yout;
        bal0_att = bal0_att + yout
      }
	}
}

/*
rule Inc_AMM_bal_inst {
    exists a : address .  //redundant
      << a : AMM . swap_def(10 , True , 0) $ 0 >>		
        bal0_AMM != old(bal0_AMM)
}
*/

/*
rule Dec_AMM_bal_inst {
    exists a : address .  //redundant
    exists args: calldataargs .
    exists f: method .
      << a : AMM . swap_def(3 , True , 0) $ 0 >>		
        bal0_AMM < old(bal0_AMM)
}*/

/*
rule Increase_AMM_bal {
    exists a : address .  //redundant
    exists args: calldataargs .
    exists f: method .
      << a : AMM . f(args) $ 0 >>		
        bal0_AMM > old(bal0_AMM)
}


rule Decrease_AMM_bal {
    exists a : address .  //redundant
    exists args: calldataargs .
    exists f: method .
      << a : AMM . f(args) $ 0 >>		
        bal0_AMM < old(bal0_AMM)
}
*/
/*
rule P1_false {
  forall a : address .  
    << a : AMM . swap_def(0 , False , 0) $ 0 >>		
      bal0_AMM > old(bal0_AMM)
}

rule P1_true {
  counter < 0 ->
    (forall a : address .  
      << a : AMM . swap_def(0 , False , 0) $ 0 >>		
        bal0_AMM >= old(bal0_AMM))
}
*/

// rule Non_depletion {
//   bal0_AMM > 0
//   &&
//   bal1_AMM > 0
// }


// False with Ints
// True with Reals
rule Constant_product {
    counter > 0 ->
      forall a : address .  //redundant
      forall args: calldataargs .
      forall f: method .
      forall msgvalue: int .
        << a : AMM . f(args) $ msgvalue >>		
          bal0_AMM*bal1_AMM == old(bal0_AMM*bal1_AMM)
}
