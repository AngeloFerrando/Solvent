contract VestingWallet {
    const address beneficiary
    const int start
    const int duration
    int released        // total amount sent to the beneficiary
    int totalAllocation // total amount received

    int amount          // local variable used in release
    int vested_amount   // local variable used in release

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


property  owner_wd_started_live {
    Forall xa
    [
      st.balance>0 && st.released==0 && st.block.number>st.start
        ->
      Exists tx [1, st.beneficiary]
      [
        ((app_tx_st.balance[st.beneficiary] > st.balance[st.beneficiary]))
      ]
    ]
}

