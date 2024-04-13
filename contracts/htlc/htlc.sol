contract HTLC {

    bool committed
    const int timeout
    const address owner
    const address recipient
    hash hashlock

    constructor(int t, address r) payable {
        timeout = t;
        owner = msg.sender;
        recipient = r
    }

    function commit(hash h) payable {
        require (not committed);
        require (msg.value > 0);
        require (msg.sender==owner);
        committed = true;
        hashlock = h
    }

    function reveal(secret s) {
        require (committed);
        if (hashlock == sha256(s)) {
            recipient!balance
        }
    }

    function timeout() {
        require(committed && block.number > timeout);
        msg.sender!balance
    }   
}

// UNSAT
property p1_live { 
    Forall xa
    [
        xa==st.owner && st.balance>0 && st.committed
        ->
        Exists tx [1, xa]
        [
            ((app_tx_st.balance[st.recipient] >= st.balance[st.recipient] + st.balance))
        ]
    ]
}

property p2_nonlive { 
    Forall xa
    [
        xa==st.recipient && st.balance>0 && st.committed
        ->
        Exists tx [1, xa]
        [
            ((app_tx_st.balance[xa] >= st.balance[xa] + st.balance))
        ]
    ]
}

// LIVE
property p3_live { 
    Forall xa
    [
        st.balance>0 && st.committed && st.block.number>st.timeout
        ->
        Exists tx [1, xa]
        [
            ((app_tx_st.balance[xa] >= st.balance[xa] + st.balance))
        ]
    ]
}
