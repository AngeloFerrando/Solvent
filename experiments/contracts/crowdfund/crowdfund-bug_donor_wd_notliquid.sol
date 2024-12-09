contract Crowdfund {
    int immutable end_donate;  // last block in which users can donate
    int immutable target;      // amount of ETH that must be donated for the crowdfunding to be succesful
    address immutable owner;   // receiver of the donated funds
    mapping (address => int) donors;
    bool target_reached;       // true when the target is reached

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
        owner.transfer(balance)
    }

    function wdDonor() { 
        require (block.number > end_donate);
        require (balance < target); // BUG: should check target_reached
        msg.sender.transfer(donors[msg.sender]);
        donors[msg.sender] = 0
    }
}

// if target is reached, the owner can withdraw at least the target after the deadline
property  donor_wd_notliquid {
    Forall xa
    [
      not target_reached && block.number>end_donate
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] >= balance[xa]+donors[xa]))
      ]
    ]
}

// if threshold is reached, the owner can withdraw at least the target after the deadline
// not liquid because of bug
