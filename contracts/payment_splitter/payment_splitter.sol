contract PaymentSplitter {
	(address -> int) shares
	int totalShares
    (address -> int) released
	int totalReleased
    int totalReceived 
    int payment
    address owner
    int state

    constructor(o) {
        // shares = emptymap;
        // released = emptymap;
        owner = o
        // totalShares = 0;
        // totalReleased = 0;
        // state = 0
    }

    function addShares(p s) {
        require(msg.sender == owner);
        require(state == 0);
        shares[p] = shares[p] + s;
        totalShares = totalShares + s
    }

    function finalizeShares() {
        require(msg.sender == owner);
        require(state == 0);
        state = 1
    }

    function receive() payable {
        skip
    } 

    function release(a) { 
        require(shares[a] > 0);
        require(state == 1);
    
        totalReceived = balance + totalReleased;
        payment = (totalReceived * shares[a]) / totalShares - released[a];
        if (payment != 0) {
            totalReleased = totalReleased + payment;
            released[a] = released[a] + payment;
            a!payment
        }
    }
}

// ? Can_Transactions_Arrive_Any_time=False: WEAK SAT WEAK UNSAT ?
// ? Can_Transactions_Arrive_Any_time=True: STRONG SAT ?
property liquidity11a_nonliq {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa] + st.balance))
      ]
    ]
}