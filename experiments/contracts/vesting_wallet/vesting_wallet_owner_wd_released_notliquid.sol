contract VestingWallet {
    address immutable beneficiary
    int immutable start
    int immutable duration
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
        beneficiary.transfer(amount)
    }
}


property  owner_wd_released_notliquid {
    Forall xa
    [
      balance>0 && block.number>start
        ->
      Exists tx [1, beneficiary]
      [
        ((<tx>balance[beneficiary] > balance[beneficiary]))
      ]
    ]
}
