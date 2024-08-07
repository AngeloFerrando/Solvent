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
property  verifier_wd_timeout_liquid { 
    Forall xa
    [
        state==1 && block.number>timeout
        ->
        Exists tx [1, xa]
        [
            <tx>balance[verifier] >= balance[verifier] + deposit
        ]
    ]
}

// the contract is liquid (its balance can always be emptied after the deadline)
