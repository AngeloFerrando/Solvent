contract HTLC {
    int immutable timeout
    address immutable owner
    address immutable verifier

    int deposit
    int state // 0 = INIT, 1 = COMMITTED, 2 = END
    hash hashlock

    constructor(int t, address r) {
        timeout = t;
        owner = msg.sender;
        verifier = r
    }

    function commit(hash h) payable {
        require (msg.sender==owner);
        require (msg.value >= 1);
        require (state==0); // INIT
        hashlock = h;
        deposit = msg.value;
        state = 1 // COMMITTED
    }

    function reveal(secret s) {
        require (state==1); // COMMITTED
        if (hashlock == sha256(s)) {
            owner.transfer(balance)
        };
        state = 2 // END
    }

    function timeout() {
        require(block.number > timeout);
        verifier.transfer(balance);
        state = 2 // END
    }   
}

// the owner can withdraw the deposit before the deadline (by revealing the secret)
property owner_wd_live { 
    Forall xa
    [
        st.state==1 && st.block.number <= st.timeout
        ->
        Exists tx [1, st.owner]
        [
            app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.deposit
        ]
    ]
}

// any user different from the owner can transfer the deposit to the owner before the deadline (by revealing the secret) 
property notowner_wd_owner_nonlive { 
    Forall xa
    [
        st.state==1 && st.block.number <= st.timeout
        ->
        Exists tx [1, xa]
        [
            app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.balance
        ]
    ]
}

// the owner can transfer to any user different from the owner the deposit before the deadline (by revealing the secret) 
property owner_wd_notowner_nonlive { 
    Forall xa
    [
        st.state==1 && st.block.number <= st.timeout
        ->
        Exists tx [1, st.owner]
        [
            app_tx_st.balance[xa] >= st.balance[xa] + st.balance
        ]
    ]
}

// the verifier can withdraw the deposit after the deadline
property verifier_wd_timeout_live { 
    Forall xa
    [
        st.state==1 && st.block.number>st.timeout
        ->
        Exists tx [1, xa]
        [
            app_tx_st.balance[st.verifier] >= st.balance[st.verifier] + st.deposit
        ]
    ]
}

// the contract is liquid (its balance can always be emptied after the deadline)
property liquidity_live { 
    Forall xa
    [
        st.block.number>st.timeout
        ->
        Exists tx [1, xa]
        [
            app_tx_st.balance==0
        ]
    ]
}
