contract PaymentSplitter {
    address owner;

    mapping (address => int) shares;     // number of shares of each user
    mapping (address => int) released;   // amount of ETH released to each user

    uint totalShares;     // total number of shares
    uint totalReleased;   // total amount of ETH sento to users
    uint totalReceived;   // total amount of ETH received
    uint payment;
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
        require(payment >= 0);
        totalReleased = totalReleased + payment;
        released[a] = released[a] + payment;
        a.transfer(payment)
        // if (payment > 0) {
        //     totalReleased = totalReleased + payment;
        //     released[a] = released[a] + payment;
        //     a.transfer(payment)
        // }
    }
}

// rule Anyone_wd_ge_liquid_True {
//     forall addr: address .
//     ((((balance + totalReleased) * shares[addr]) > (released[addr] * totalShares)) && state==1) ->
//     (exists f: method .
//     exists args: calldataargs .
//     exists msgvalue : int .
//     (<< addr : PaymentSplitter . f(args) $ msgvalue >>		
//               (balance[addr] > old(balance[addr]))
//     ))
// }



rule Anyone_wd_ge_liquid_False {
    forall addr: address .
    ((((balance + totalReleased) * shares[addr]) > (released[addr] * totalShares)) && state==1) ->
    (exists f: method .
    exists args: calldataargs .
    exists msgvalue : int .
    (<< addr : PaymentSplitter . f(args) $ msgvalue >>		
              (balance[addr] > old(balance[addr]) + 3)
    ))
}

/*
// anyone can withdraw the corresponding releasable funds after the finalization of shares
property anyone_wd_ge_liquid {
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
property anyone_wd_releasable_liquid {
    Forall xa
    [
      state==1 && shares[xa]>0
        ->
      Exists tx [1, xa]
      [
        (<tx>balance[xa] >= balance[xa] + (((balance + totalReleased) * shares[xa]) / totalShares) - released[xa])
      ]
    ]
}

// at any time, any user can withdraw the whole contract balance (should be false)
// ? Can_Transactions_Arrive_Any_time=False: WEAK SAT WEAK UNSAT ?
// ? Can_Transactions_Arrive_Any_time=True: STRONG SAT ?
property anyone_wd_nonliquid {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa] + balance))
      ]
    ]
}
*/