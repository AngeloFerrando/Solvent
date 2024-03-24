contract Auction {
    int deadline
    int min_bid
    address winner  
    address seller

    constructor(b d m) { // FIXME: if parameter a is used instead of b -> NameError: name 'constructor_a' is not defined
        seller = b;
        deadline = d;
        min_bid = m
    }
     
    function bid(a) payable {
        require (msg.value >= min_bid);
        // the current bid is greater than the previous ones 
        // this guarantees that the contract balance is strictly positive 
        require (msg.value > balance);     
        require (a != 0);
        
        // the previous maximum bid is returned to the previous winner
        winner!(balance-msg.value);
        
        // the new winner is set to the current (highest) bidder
        winner = a
    }    
    
    function close() {
        require (msg.sender == seller);
        require (block.number > deadline);
        seller!balance
    }
}

// should be true: seller can withdraw the balance after the deadline
property sellerCanWithdraw_liq {
    Forall xa
    [
      st.winner!=0 && st.balance>0
        ->
      Exists tx [1, st.seller]
      [
        ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}

// should be false?: the seller can have already fired close 
property sellerCanWithdraw_nonliq1 {
    Forall xa
    [
      st.winner!=0 && st.block.number>deadline
        ->
      Exists tx [1, st.seller]
      [
        ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}

// should be false: if the winner has not been set, the contract balance could be 0
property sellerCanWithdraw_nonliq2 {
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

// should be false?: only the seller can fire the close transaction
property sellerCanWithdraw_nonliq3 {
    Forall xa
    [
      st.winner!=0
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}

// should be false: only the seller can increase its balance
property sellerCanWithdraw_nonliq4 {
    Forall xa
    [
      st.winner!=0
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] > st.balance[xa]))
      ]
    ]
}