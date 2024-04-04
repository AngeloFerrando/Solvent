contract VestingWallet {
    int released
    address beneficiary
    int start
    int duration

    int amount
    int vested_amount
    int totalAllocation

    constructor(address b, int t, int d) {
        require (d > 0);
	    beneficiary = b;
        start = t;
        duration = d
    }

    function receive() payable { 
        skip
    }

    function release() {
        totalAllocation = balance + released;

        if (block.number < start) {
            vested_amount = 0
        }
        else {
            if (block.number > start + duration) {
                vested_amount = totalAllocation
            }
            else {
                vested_amount = (totalAllocation * (block.number - start)) / duration
            }
        };

        amount = vested_amount - released;
        released = released + amount;
        beneficiary!amount
    }
}

property liq1 {
    Forall xa
    [
      xa==st.beneficiary && st.balance>0 && released==0 && st.block.number>st.start+st.duration
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}

property liq2 {
    Forall xa
    [
      xa==st.beneficiary && st.balance>0 && released==0 && st.block.number>st.start
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}
