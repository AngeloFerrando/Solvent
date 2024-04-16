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
        require (donors[msg.sender] > 0);
        msg.sender!donors[msg.sender];
        donors[msg.sender] = 0
    }
}

// if target is reached, the owner can withdraw at least the target after the deadline
property owner_wd_live {
    Forall xa
    [
      st.target_reached && st.balance>=st.target && st.block.number > st.end_donate
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}

// if threshold is not reached, donors can withdraw their donations after the end_donate
// this is false, because a coinbase or selfdestruct can increase the balance
property donor_wd_notlive {
    Forall xa
    [
      st.donors[xa]>0 && (not target_reached) && st.block.number>st.end_donate
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] >= st.balance[xa]+st.donors[xa]))
      ]
    ]
}

// if threshold is reached, the owner can withdraw at least the target after the deadline
property liquidity_live {
    Forall xa
    [
      st.balance>0 && st.block.number > st.end_donate
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance==0)
      ]
    ]
}

// if there is some donor with enough tokens, then the campaign can be successful
property can_reach_target_live {
    Forall xa
    [
      st.balance[xa] > st.target && st.block.number <= st.end_donate
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance >= app_tx_st.target)
      ]
    ]
}
