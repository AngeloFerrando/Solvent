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
property  owner_wd_balance_geq_nonliquid {
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
