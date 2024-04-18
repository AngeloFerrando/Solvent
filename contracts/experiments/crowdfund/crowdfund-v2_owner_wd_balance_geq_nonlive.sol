contract Crowdfund {
    const int end_donate              // deadline for donations
    const int target                  // the campaign is successful is this target is reaches 
    const address owner               // beneficiary of the campaign
    const int min_donation            // minimum donation
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
       	owner!balance;
        owner_withdrawn = true
    }

    function wdDonor() {
        require (block.number > end_donate);
        require (received<target);
       	msg.sender!funds[msg.sender];
       	funds[msg.sender] = 0
    }
}

// if threshold is reached, the owner can withdraw at least the target after the deadline
property  owner_wd_balance_geq_nonlive {
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
