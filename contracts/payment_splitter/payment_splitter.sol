contract PaymentSplitter {
    const address owner

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
            a!payment
        }
    }
}

// anyone can withdraw the corresponding releasable funds after the finalization of shares
property anyone_wd_ge_live {
    Forall xa
    [
      (((st.balance + st.totalReleased) * st.shares[xa]) > (st.released[xa] * st.totalShares)) && st.state==1
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance[xa] > st.balance[xa])
      ]
    ]
}

// anyone can withdraw the corresponding releasable funds after the finalization of shares
property anyone_wd_releasable_live {
    Forall xa
    [
      st.state==1 && st.shares[xa]>0
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance[xa] >= st.balance[xa] + (((st.balance + st.totalReleased) * st.shares[xa]) / st.totalShares) - st.released[xa])
      ]
    ]
}

// at any time, any user can withdraw the whole contract balance (should be false)
// ? Can_Transactions_Arrive_Any_time=False: WEAK SAT WEAK UNSAT ?
// ? Can_Transactions_Arrive_Any_time=True: STRONG SAT ?
property anyone_wd_nonlive {
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
