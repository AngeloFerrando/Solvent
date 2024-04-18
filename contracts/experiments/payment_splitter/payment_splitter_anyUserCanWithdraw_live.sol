contract PaymentSplitter {
    const address owner

    mapping (address => int) shares     // number of shares of each user
    mapping (address => int) released   // amount of ETH released to each user

    int totalShares     // total number of shares
    int totalReleased   // total amount of ETH released
    int totalReceived   // total amount of ETH received
    int payment
    int state // 0 = shares can be added, 1 = shares are finalized and funds can be released

    constructor(address o) {
        owner = o
    }

    function addShares(address p, int s) {
        require(msg.sender == owner);
        require(state == 0);
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
property  anyUserCanWithdraw_live {
    Forall xa
    [
      released[xa]==0 && shares[xa]>0 && state==1
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}
