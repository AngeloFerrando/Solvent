contract PaymentSplitter {
    address immutable owner

    mapping (address => int) shares     // number of shares of each user
    mapping (address => int) released   // amount of ETH released to each user

    int totalShares     // total number of shares
    int totalReleased   // total amount of ETH sento to users
    int totalReceived   // total amount of ETH received
    int payment
    int state // 0 = shares can be added, 1 = shares are finalized and funds can be released

    constructor() {
        owner = msg.sender
    }

    function addShares(address p, int s) {
        require(msg.sender == owner);
        require(state == 0);
        require(s > 0);
        shares[p] = shares[p] + s;
        totalShares = totalShares + s
    }

    function finalizeShares() {
        require(msg.sender == owner);
        require(state == 0);
        state = 1 // shares are finalized and funds can be released
    }

    // the contract can receive ETH at any time
    function receive() payable { 
      skip 
    }

    function release(address a) { 
        require(shares[a] > 0);
        require(state == 1);
    
        totalReceived = balance + totalReleased;
        payment = ((totalReceived * shares[a]) / totalShares) - released[a];
        if (payment > 0) {
            totalReleased = totalReleased + payment;
            released[a] = released[a] + payment;
            a.transfer(payment)
        }
    }
}

// anyone can withdraw the corresponding releasable funds after the finalization of shares
property  anyone_wd_ge_liquid {
    Forall xa
    [
      (((balance + totalReleased) * shares[xa]) > (released[xa] * totalShares)) && state==1
        ->
      Exists tx [1, xa]
      [
        (<tx>balance[xa] > balance[xa])
      ]
    ]
}

// anyone can withdraw the corresponding releasable funds after the finalization of shares
