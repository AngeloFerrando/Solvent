contract Auction {
    int deadline
    int min_bid
    int current_bid
    address winner  
    address seller
    bool closed

    constructor(address b, int d, int m) { // FIXME: if parameter a is used instead of b -> NameError: name 'constructor_a' is not defined
        seller = b;
        deadline = d;
        min_bid = m;
        current_bid = 0;
        closed = false
    }
     
    function bid(address a) payable {
        //require (block.number <= deadline);   // Auction closes after deadline
        require(not closed);
        //require (msg.sender != seller);       // Can the seller bid?
        require (msg.value >= min_bid);

        // the current bid is greater than the previous ones 
        // this guarantees that the contract balance is strictly positive 
        //require (msg.value > balance);     
        require (msg.value > current_bid); // EL change
        
        //require (a != 1);

        // the previous maximum bid is returned to the previous winner
        //winner!(balance-msg.value);
        winner!current_bid; // EL change
        
        
        // the new winner is set to the current (highest) bidder
        winner = a;
        //winner = msg.sender;  // EL change

        // update current_bid
        current_bid = msg.value   // EL change
    }    
    
    function close() {
        require (not closed);
        require (msg.sender == seller);
        require (block.number > deadline);
        closed = true;
        seller!balance
    }
}


// EL: STRONG SAT
// should be false: if the winner has not been set, the contract balance could be 0
property sellerCanWithdraw_nonlive4 {
    Forall xa
    [
      st.block.number>deadline
        ->
      Exists tx [1, st.seller]
      [
        ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}

