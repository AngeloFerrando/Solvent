contract HTLC {

    int timeout
    address owner
    address verifier
    address hashlock

    constructor(int t, address r) payable {
        require (msg.value > 0);
        timeout = t;
        owner = msg.sender;
        verifier = r;
        // TODO: use parameter hash h
        hashlock = msg.sender
    }

    function reveal() {
        if (hashlock == msg.sender) {
            verifier!balance
        }
    }

    function timeout() {
        require(block.number > timeout);
        msg.sender!balance

    }   
}

// UNSAT
property  p2_nonlive { 
    Forall xa
    [
        xa==st.verifier && st.balance>0
        ->
        Exists tx [1, xa]
        [
            ((app_tx_st.balance[xa] >= st.balance[xa] + st.balance))
        ]
    ]
}

