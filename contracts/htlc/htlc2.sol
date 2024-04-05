contract HTLC {

    int timeout
    address owner
    address recipient
    address hashlock

    constructor(int t, address r) payable {
        require (msg.value > 0);
        timeout = t;
        owner = msg.sender;
        recipient = r;
        // TODO: use parameter hash h
        hashlock = msg.sender
    }

    function reveal() {
        if (hashlock == msg.sender) {
            recipient!balance
        }
    }

    function timeout() {
        require(block.number > timeout);
        msg.sender!balance

    }   
}

// UNSAT
property p1_liq { 
    Forall xa
    [
        xa==st.owner && st.balance>0
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
        xa==st.recipient && st.balance>0
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
        st.balance>0 && st.block.number>st.timeout
        ->
        Exists tx [1, xa]
        [
            ((app_tx_st.balance[xa] >= st.balance[xa] + st.balance))
        ]
    ]
}
