contract HTLC {

    bool committed
    int timeout
    address owner
    address recipient
    int hashlock

    constructor(int t, address r) payable {
        timeout = t;
        owner = msg.sender;
        recipient = r
    }

    function commit(hash h) payable {
        require (!committed);
        require (msg.value > 0);
        committed = true;
        hashlock = h;
        require (msg.sender==owner);
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
property p1_liq { 
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

property p2_nonliq { 
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

property p3_liq { 
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
