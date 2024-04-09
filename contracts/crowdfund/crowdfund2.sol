contract Crowdfund {
    int deadline              // deadline for donations
    int target                // the campaign is successful is this target is reaches 
    address owner             // beneficiary of the campaign
    int min_donation          // minimum donation
    (address -> int) funds    // keeps track of the donations
    bool success              // campaign successful
    bool owner_withdrawn      // has the owner withdrawn the funds?

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
        if (balance >= target) {
            success = true
        }
    }

    function wdOwner() {
        require (block.number > deadline);
        require (success && not owner_withdrawn);
       	owner!balance;
        owner_withdrawn = true
    }

    function wdDonor() {
        require (block.number > deadline);
        require (not success);
       	msg.sender!funds[msg.sender];
       	funds[msg.sender] = 0
    }
}

// should be true??: if there is donor with enough tokens, then campaign can be successful
property success_live {
    Forall xa
    [
      st.balance[xa] > st.target && st.block.number <= st.deadline
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.success)
      ]
    ]
}
// should be false??: seller cannot withdraw 1000 (e.g. if target is < 1000)
property ownerCanWithdraw4_nonlive {
    Forall xa
    [
      success && st.block.number > st.deadline
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= 1000))
      ]
    ]
}
