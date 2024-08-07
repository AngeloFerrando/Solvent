contract Auction {
    int immutable deadline;
    int immutable min_bid;
    address immutable seller;

    address winner;
    int current_bid; // current maximum bit
    bool closed;     // becomes true when the auction is closed

    constructor(address b, int d, int m) { // FIXME: if parameter a is used instead of b -> NameError: name 'constructor_a' is not defined
        // require(b!=0 && m>0 && d>0);
        seller = b;
        deadline = d;
        min_bid = m;
        closed = false
    }
     
    function bid() payable {
        require(!closed);
        require (msg.value >= min_bid);
        // the current bid is greater than the previous ones 
        // this guarantees that the contract balance is strictly positive 
        require (msg.value > current_bid);
     
        // the previous maximum bid is returned to the previous winner
        winner.transfer(current_bid);
        
        // the new winner is set to the current (highest) bidder
        winner = msg.sender;
        current_bid = msg.value
    }    
    
    function close() {
        require (!closed);
        require (msg.sender == seller);
        require (block.number > deadline);
        closed = true;
        seller.transfer(balance)
    }
}

// the seller can withdraw the current bid after the deadline
property seller_wd_liquid {
    Forall xa
    [
      winner!=0 && balance>0 && block.number>deadline && (not closed)
        ->
      Exists tx [1, seller]
      [
        (<tx>balance[seller] >= balance[seller] + current_bid) && (current_bid >= 0)
      ]
    ]
}

// the old winner can withdraw the current bid
property old_winner_wd_liquid {
    Forall xa
    [
      winner!=0 && not closed
        ->
      Exists tx [1, xa]
      [
        (<tx>balance[winner] == balance[winner] + current_bid)
      ]
    ]
}

// the seller can withdraw the bid after the deadline
property seller_wd2_liquid {
    Forall xa
    [
      winner!=0 && balance>0 && block.number>deadline && (not closed)
        ->
      Exists tx [1, seller]
      [
        (<tx>balance[seller] >= balance[seller] + current_bid) && (current_bid >= min_bid)
      ]
    ]
}

// the seller can always withdraw something (should be false before the deadline) 
property seller_wd_early_nonliquid {
    Forall xa
    [
      winner!=0 && balance>0 && closed==false
        ->
      Exists tx [1, seller]
      [
        (<tx>balance[seller] > balance[seller])
      ]
    ]
}

// the seller can withdraw something in any state (should be false: the contract can be already closed)
property seller_wd_closed_nonliquid {
    Forall xa
    [
      winner!=0 && balance>0 && block.number>deadline 
        ->
      Exists tx [1, seller]
      [
        (<tx>balance[seller] > balance[seller])
      ]
    ]
}

// the seller can withdraw something in any state (should be false: if the winner has not been set, the contract balance could be 0)
property seller_wd_nowinner_nonliquid {
    Forall xa
    [
      block.number>deadline
        ->
      Exists tx [1, seller]
      [
        (<tx>balance[seller] > balance[seller])
      ]
    ]
}

// the close transaction can be fired by someone who is not the seller (should be false) 
property nonseller_wd_nonliquid {
    Forall xa
    [
      winner!=0
        ->
      Exists tx [1, xa]
      [
        xa != seller && (<tx>balance[seller] > balance[seller])
      ]
    ]
}

// the extra budget can always be redeemed by the seller
property no_frozen_funds_nonliquid {
    Forall xa
    [
      closed
        ->
      Exists tx [1, xa]
      [
        <tx>balance[seller] >= balance[seller] + balance
      ]
    ]
}