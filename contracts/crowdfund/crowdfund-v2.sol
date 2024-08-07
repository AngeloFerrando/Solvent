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
property owner_wd_liquid {
    Forall xa
    [
      received>=target && (not owner_withdrawn) && block.number > end_donate
        ->
      Exists tx [1, owner]
      [
        ((<tx>balance[owner] >= balance[owner] + target))
      ]
    ]
}

// if threshold is not reached, donors can withdraw their donations after the end_donate
property donor_wd_liquid {
    Forall xa
    [
      funds[xa]>0 && received<target && block.number>end_donate
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] >= balance[xa]+funds[xa]))
      ]
    ]
}

// the owner can withdraw twice (should be false)
property owner_wd_twice_nonliquid {
    Forall xa
    [
      received>=target && block.number > end_donate
        ->
      Exists tx [1, owner]
      [
        ((<tx>balance[owner] >= balance[owner] + target))
      ]
    ]
}

// the owner can withdraw if the contract balance exceeds the target (should be false: a coinbase tx can increase the contract balance)
property owner_wd_balance_geq_nonliquid {
    Forall xa
    [
      balance >= target && block.number > end_donate
        ->
      Exists tx [1, owner]
      [
        ((<tx>balance[owner] >= balance[owner] + target))
      ]
    ]
}

// if there is some donor with enough tokens, then the campaign can be successful
property can_reach_target_liquid {
    Forall xa
    [
      balance[xa] >= target && block.number <= end_donate
        ->
      Exists tx [1, xa]
      [
        (<tx>received>=target)
      ]
    ]
}

// should be false: seller cannot withdraw 1000 (e.g. if target is < 1000)
property owner_wd_toomuch_nonliquid {
    Forall xa
    [
      received>=target && block.number > end_donate
        ->
      Exists tx [1, owner]
      [
        ((<tx>balance[owner] >= 1000))
      ]
    ]
}

// after the owner withdraws, donors can redeem their donations (should be false: e.g., balance is zero)
property donor_wd_after_owner_nonliquid {
    Forall xa
    [
      funds[xa]>0 && balance<target && block.number>end_donate
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] >= balance[xa] + funds[xa]))
      ]
    ]
}
