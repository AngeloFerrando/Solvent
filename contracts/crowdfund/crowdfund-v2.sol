contract Crowdfund {
    int immutable end_donate              // deadline for donations
    int immutable target                  // the campaign is successful is this target is reaches 
    address immutable owner               // beneficiary of the campaign
    int immutable min_donation            // minimum donation
    mapping (address => int) funds    // keeps track of the donations
    int received                      // total amount received (excluding coinbase/selfdestruct)
    bool owner_withdrawn              // has the owner withdrawn the funds?

    constructor(int d, int t, address o, int m) {
        owner = o;
        end_donate = d; 
        target = t;
        min_donation = m;
        require (m < target)
    }

    function donate() payable {
        require (block.number <= end_donate);
        require (msg.value>=min_donation);
       	funds[msg.sender] = funds[msg.sender] + msg.value;
        received = received + msg.value
    }

    function wdOwner() {
        require (block.number > end_donate);
        require (received>=target && not owner_withdrawn);
       	owner.transfer(balance);
        owner_withdrawn = true
    }

    function wdDonor() {
        require (block.number > end_donate);
        require (received<target);
       	msg.sender.transfer(funds[msg.sender]);
       	funds[msg.sender] = 0
    }
}

// if threshold is reached, the owner can withdraw at least the target after the deadline
property owner_wd_live {
    Forall xa
    [
      st.received>=st.target && (not st.owner_withdrawn) && st.block.number > st.end_donate
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// if threshold is not reached, donors can withdraw their donations after the end_donate
property donor_wd_live {
    Forall xa
    [
      st.funds[xa]>0 && st.received<st.target && st.block.number>st.end_donate
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] >= st.balance[xa]+st.funds[xa]))
      ]
    ]
}

// the owner can withdraw twice (should be false)
property owner_wd_twice_nonlive {
    Forall xa
    [
      st.received>=st.target && st.block.number > st.end_donate
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// the owner can withdraw if the contract balance exceeds the target (should be false: a coinbase tx can increase the contract balance)
property owner_wd_balance_geq_nonlive {
    Forall xa
    [
      st.balance >= st.target && st.block.number > st.end_donate
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// if there is some donor with enough tokens, then the campaign can be successful
property can_reach_target_live {
    Forall xa
    [
      st.balance[xa] >= st.target && st.block.number <= st.end_donate
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.received>=st.target)
      ]
    ]
}

// should be false: seller cannot withdraw 1000 (e.g. if target is < 1000)
property owner_wd_toomuch_nonlive {
    Forall xa
    [
      st.received>=st.target && st.block.number > st.end_donate
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= 1000))
      ]
    ]
}

// after the owner withdraws, donors can redeem their donations (should be false: e.g., balance is zero)
property donor_wd_after_owner_nonlive {
    Forall xa
    [
      st.funds[xa]>0 && st.balance<st.target && st.block.number>st.end_donate
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] >= st.balance[xa] + st.funds[xa]))
      ]
    ]
}
