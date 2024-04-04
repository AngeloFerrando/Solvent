contract Crowdfund {
    int deadline                        // deadline for donations
    int target                          // the campaign is successful is this target is reaches 
    address owner                       // beneficiary of the campaign
    int min_donation                    // minimum donation
    (address -> int) funds             // keeps track of the donations

    constructor(int d, int t, address o, int m) {
        owner = o;
        deadline = d; 
        target = t;
        min_donation = m
    }

    function deposit(address a) payable {
        require (block.number <= deadline);
        require (msg.value>=min_donation);
       	funds[msg.sender] = funds[msg.sender] + msg.value
    }

    function finalize() {
        require (block.number > deadline);
        require (balance >= target);
       	owner!balance
    }

    function withdraw() {
        require (block.number > deadline);
        require (balance < target);
       	msg.sender!funds[msg.sender];
       	funds[msg.sender] = 0
    }
}


// should be true: seller can withdraw the balance after the deadline
property ownerCanWithdraw_liq {
    Forall xa
    [
      st.balance >= st.target && st.block.number > st.deadline
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}