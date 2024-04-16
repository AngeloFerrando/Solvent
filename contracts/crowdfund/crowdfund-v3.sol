contract Crowdfund {
    int end_donate                    // deadline for donations
    int target                        // the campaign is successful is this target is reaches 
    address owner                     // beneficiary of the campaign
    int min_donation                  // minimum donation
    mapping (address => int) funds    // keeps track of the donations
    bool success                      // campaign successful
    bool owner_withdrawn              // has the owner withdrawn the funds?

    constructor(int d, int t, address o, int m) {
        owner = o;
        end_donate = d; 
        target = t;
        min_donation = m;
        require (m < target)
    }

    function deposit() payable {
        require (block.number <= end_donate);
        require (msg.value>=min_donation);
       	funds[msg.sender] = funds[msg.sender] + msg.value;
        if (balance >= target) {
            success = true
        }
    }

    function wdOwner() {
        require (block.number > end_donate);
        require (success && not owner_withdrawn);
       	owner!balance;
        owner_withdrawn = true
    }

    function wdDonor() {
        require (block.number > end_donate);
        require (not success);
       	msg.sender!funds[msg.sender];
       	funds[msg.sender] = 0
    }
}

// if there is some donor with enough tokens, then the campaign can be successful
property can_reach_target_live {
    Forall xa
    [
      st.balance[xa] > st.target && st.block.number <= st.end_donate
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.success)
      ]
    ]
}

// the owner can withdraw 1000 (should be false: e.g., if target is < 1000)
property owner_wd_toomuch_nonlive {
    Forall xa
    [
      st.success && st.block.number > st.end_donate
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= 1000))
      ]
    ]
}
