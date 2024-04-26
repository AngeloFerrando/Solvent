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
            verifier.transfer(balance)
        }
    }

    function timeout() {
        require(block.number > timeout);
        msg.sender.transfer(balance)

    }   
}

// UNSAT
property p1_live { 
    Forall xa
    [
        xa==owner && balance>0
        ->
        Exists tx [1, xa]
        [
            ((<tx>balance[verifier] >= balance[verifier] + balance))
        ]
    ]
}

property p2_nonlive { 
    Forall xa
    [
        xa==verifier && balance>0
        ->
        Exists tx [1, xa]
        [
            ((<tx>balance[xa] >= balance[xa] + balance))
        ]
    ]
}

property p3_live { 
    Forall xa
    [
        balance>0 && block.number>timeout
        ->
        Exists tx [1, xa]
        [
            ((<tx>balance[xa] >= balance[xa] + balance))
        ]
    ]
}
