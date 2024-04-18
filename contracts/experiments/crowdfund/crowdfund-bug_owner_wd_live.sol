contract Crowdfund {
    const int end_donate    // last block in which users can donate
    const int target        // amount of ETH that must be donated for the crowdfunding to be succesful
    const address owner     // receiver of the donated funds
    mapping (address => int) donors
    bool target_reached     // true when the target is reached

    constructor(address owner_, int end_donate_, int target_) {
        owner = owner_;
        end_donate = end_donate_;
	      target = target_
    }
    
    function donate() payable {
        require (block.number <= end_donate);
        donors[msg.sender] = donors[msg.sender] + msg.value;
        if (balance >= target) { target_reached = true }
    }

    function wdOwner() {
        require (target_reached && block.number > end_donate);
        owner!balance
    }

    function wdDonor() { 
        require (block.number > end_donate);
        require (balance < target); // BUG: should check target_reached
        msg.sender!donors[msg.sender];
        donors[msg.sender] = 0
    }
}

// if target is reached, the owner can withdraw at least the target after the deadline
property  owner_wd_live {
    Forall xa [
      st.target_reached && st.balance>=st.target && st.block.number > st.end_donate
      ->
      Exists tx [1, st.owner] 
        [ app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target ]
    ]
}

// if threshold is not reached, donors can withdraw their donations after the end_donate
// this is false, because a coinbase or selfdestruct can increase the balance
