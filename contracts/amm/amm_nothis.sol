
contract AMM {
  int counter;
	mapping (address => int) bal0;
	mapping (address => int) bal1;
  uint bal0_AMM;
  uint bal1_AMM;
    bool tout;
    uint yout;

	constructor(uint x0, uint x1) {
        require(x0 > 0 && x1 > 0);
        //bal0[msg.sender] = bal0[msg.sender] - x0;
        //bal1[msg.sender] = bal1[msg.sender] - x1;  
        bal0[msg.sender] = 100;
        bal1[msg.sender] = 50;  
        bal0_AMM = x0;
        bal1_AMM = x1;
        counter = 0
    }

    /* tin is 0 if T0; 1 if T1 */
	function swap(uint xin, bool tin, uint ymin) {
    require(bal0_AMM > 0 && bal1_AMM > 0);
		require(xin > 0);
		tout = not tin;
    counter = counter + 1;
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


// rule Test_true {
//   forall a : address .  
//     << a : AMM . swap(0 , False , 0) $ 0 >>		
//       true
// }

// rule Test_false {
//   forall a : address .  
//     << a : AMM . swap(0 , False , 0) $ 0 >>		
//       false
// }


// rule P1_false {
//   forall a : address .  
//     << a : AMM . swap(0 , False , 0) $ 0 >>		
//       bal0_AMM > old(bal0_AMM)
// }


// if swap reverts than bal0_AMM does not increase
// rule P2_false { 
//   forall a : address .  
//     << a : AMM . swap(1 , False , 0) $ 0 >>		
//       bal0_AMM > old(bal0_AMM)
// }

// if not revert, than bal0_AMM always increases of xin
// rule P2b_true {
//   forall a : address .  
//     << a : AMM . swap(1 , False , 0) $ 0 >>		
//     !lastReverted ->
//       bal0_AMM > old(bal0_AMM)
// }

// rule è sempre possibile fare un gain (falso con Int, vero con i Real; assumiamo che i prezzi siano 1 e che l'AMM sia balanced, ovvero stesso numero di token)


// rule P3_false {
//   forall a : address .  
//     << a : AMM . swap(0 , False , 0) $ 0 >>		
//       bal1_AMM < old(bal1_AMM)
// }

// if swap reverts than bal1_AMM does not increase
// rule P4_false {
//   forall a : address .  
//     << a : AMM . swap(1 , False , 0) $ 0 >>		
//       bal1_AMM < old(bal1_AMM)
// }

// // with Ints, we can have yout = 0 due to approximations
// rule P4b_false {
//   forall a : address .  
//     << a : AMM . swap(1 , False , 0) $ 0 >>		
//       !lastReverted 
//         ->
//       bal1_AMM < old(bal1_AMM)
// }

// rule P4c_true {
//   forall a : address .  
//     << a : AMM . swap(1 , False , 1) $ 0 >>		
//       !lastReverted 
//         ->
//       bal1_AMM < old(bal1_AMM)
// }


// False with Ints
// True with Reals
// rule Constant_product {
//     counter > 0 ->
//       forall a : address .  //redundant
//       forall args: calldataargs .
//       forall f: method .
//       forall msgvalue: int .
//         << a : AMM . f(args) $ msgvalue >>		
//           bal0_AMM*bal1_AMM == old(bal0_AMM*bal1_AMM)
// }

rule Constant_product_violation {
    counter > 0 ->
      exists a : address .  //redundant
      exists args: calldataargs .
      exists f: method .
      exists msgvalue: int .
        << a : AMM . f(args) $ msgvalue >>		
          bal0_AMM*bal1_AMM != old(bal0_AMM*bal1_AMM)
}