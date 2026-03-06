contract LP {
	mapping (address => int) balanceOf0; // user’s balance in token T0 
	mapping (address => int) balanceOf1;

	mapping (address => int) credits0; 	// credits in token T0
	mapping (address => int) debts0;	// debts in token T0

	mapping (address => int) credits1; 	// credits in token T1
	mapping (address => int) debts1;	// debts in token T1

	int balance0; // contract balance in token T0
	int balance1;

	function deposit0(int n_d0) {
        require(n_d0 > 0);
		require(balanceOf0[msg.sender] >= n_d0);
        credits0[msg.sender] = credits0[msg.sender] + n_d0;
        balance0 = balance0 + n_d0; 
        balanceOf0[msg.sender] = balanceOf0[msg.sender] - n_d0
    }

	function borrow0(int n_b0) {
        require(n_b0 > 0);
		require(balance0 >= n_b0);
		require(credits1[msg.sender] - debts0[msg.sender] - debts1[msg.sender] >= n_b0); // sender collateralized
		balance0 = balance0  - n_b0;
        debts0[msg.sender] = debts0[msg.sender] + n_b0;
        balanceOf0[msg.sender] = balanceOf0[msg.sender] + n_b0
    }

	function deposit1(int n_d1) {
        require(n_d1 > 0);
		require(balanceOf1[msg.sender] >= n_d1);
        credits1[msg.sender] = credits1[msg.sender] + n_d1;
        balance1 = balance1 + n_d1; 
        balanceOf1[msg.sender] = balanceOf1[msg.sender] - n_d1
    }

	function borrow1(int n_b1) {
        require(n_b1 > 0);
		require(balance1 >= n_b1);
		require(credits0[msg.sender] - debts1[msg.sender] - debts0[msg.sender] >= n_b1); // sender collateralized
		balance1 = balance1  - n_b1;
        debts1[msg.sender] = debts1[msg.sender] + n_b1;
        balanceOf1[msg.sender] = balanceOf1[msg.sender] + n_b1
    }
}

// if a has no debt and a non-zero collateral, a can always borrow 

// rule No_debt_can_revert {
//     forall a : address .
//     (debts0[a] == 0 && debts0[a] == 0 && credits0[a] > 0 && balance1 > 0)
//     -> 
//     exists n : int .
//     << a : LP . borrow1(n) $ 0 >> (
//       balanceOf1[a] == old(balanceOf1[a]) + (n + 1)
//     )
// }

rule No_debt_can_revert_undercoll {
    forall a : address .
    (credits0[a] > 0 && balance1 > 0)
    -> 
    false
}