contract Crowdfund {
    const int deadline                      // deadline for donations
    const int target                        // the campaign is successful is this target is reaches 
    const address owner                     // beneficiary of the campaign
    const int min_donation                  // minimum donation
    mapping (address => int) funds    // keeps track of the donations
    int received                      // total amount received (excluding coinbase/selfdestruct)
    bool owner_withdrawn              // has the owner withdrawn the funds?

    constructor(int d, int t, address o, int m) {
        owner = o;
        deadline = d; 
        target = t;
        min_donation = m;
        require (m < target)
    }

    function deposit() payable {
        require (block.number <= deadline);
        require (msg.value>=min_donation);
       	funds[msg.sender] = funds[msg.sender] + msg.value;
        received = received + msg.value
    }

    function wdOwner() {
        require (block.number > deadline);
        require (received>=target && not owner_withdrawn);
       	owner!balance;
        owner_withdrawn = true
    }

    function wdDonor() {
        require (block.number > deadline);
        require (received<target);
       	msg.sender!funds[msg.sender];
       	funds[msg.sender] = 0
    }
}

// should be true: seller can withdraw the balance after the deadline (if threshold reached)
property ownerCanWithdraw_live {
    Forall xa
    [
      st.received>=st.target && (not st.owner_withdrawn) && st.block.number > st.deadline
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// should be false: seller cannot withdraw twice after success
property ownerCanWithdraw2_nonlive {
    Forall xa
    [
      st.received>=st.target && st.block.number > st.deadline
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// should be false: seller withdraws after success, then coinbase tx increases contract balance
property ownerCanWithdraw3_nonlive {
    Forall xa
    [
      st.balance > st.target && st.block.number > st.deadline
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// should be true: if there is donor with enough tokens, then campaign can be successful
property success_live {
    Forall xa
    [
      st.balance[xa] > st.target && st.block.number <= st.deadline
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.received>=st.target)
      ]
    ]
}
// should be false: seller cannot withdraw 1000 (e.g. if target is < 1000)
property ownerCanWithdraw4_nonlive {
    Forall xa
    [
      st.received>=st.target && st.block.number > st.deadline
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= 1000))
      ]
    ]
}


// should be true: donors can withdraw their donations after the deadline (if threshold not reached)
property donorCanWithdraw_live {
    Forall xa
    [
      st.funds[xa] > 0 && st.received<st.target && st.block.number > st.deadline
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] >= st.balance[xa] + st.funds[xa]))
      ]
    ]
}

// should be false: after owner withdraws, balance is zero and donors cannot redeem their donations
property donorCanWithdraw2_nonlive {
    Forall xa
    [
      st.funds[xa] > 0 && st.balance < st.target && st.block.number > st.deadline
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] >= st.balance[xa] + st.funds[xa]))
      ]
    ]
}
