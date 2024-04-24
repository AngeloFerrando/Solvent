contract Auction {
    int immutable deadline
    int immutable min_bid
    address immutable seller

    address winner
    int current_bid // current maximum bit
    bool closed     // becomes true when the auction is closed

    constructor(address b, int d, int m) { // FIXME: if parameter a is used instead of b -> NameError: name 'constructor_a' is not defined
        // require(b!=0 && m>0 && d>0);
        seller = b;
        deadline = d;
        min_bid = m;
        closed = false
    }
     
    function bid() payable {
        require(not closed);
        require (msg.value >= min_bid);
        // the current bid is greater than the previous ones 
        // this guarantees that the contract balance is strictly positive 
        require (msg.value > current_bid);
     
        // the previous maximum bid is returned to the previous winner
        winner!current_bid;
        
        // the new winner is set to the current (highest) bidder
        winner = msg.sender;
        current_bid = msg.value
    }    
    
    function close() {
        require (not closed);
        require (msg.sender == seller);
        require (block.number > deadline);
        closed = true;
        seller!balance
    }
}

// the seller can withdraw the current bid after the deadline
property seller_wd_live {
    Forall xa
    [
      st.winner!=0 && st.balance>0 && st.block.number>st.deadline && (not closed)
        ->
      Exists tx [1, st.seller]
      [
        (app_tx_st.balance[st.seller] >= st.balance[st.seller] + st.current_bid) && (st.current_bid >= 0)
      ]
    ]
}

// the old winner can withdraw the current bid
property old_winner_wd_live {
    Forall xa
    [
      st.winner!=0 && not closed
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance[st.winner] == st.balance[st.winner] + st.current_bid)
      ]
    ]
}

// the seller can withdraw the bid after the deadline
property seller_wd2_live {
    Forall xa
    [
      st.winner!=0 && st.balance>0 && st.block.number>st.deadline && (not closed)
        ->
      Exists tx [1, st.seller]
      [
        (app_tx_st.balance[st.seller] >= st.balance[st.seller] + st.current_bid) && (st.current_bid >= st.min_bid)
      ]
    ]
}

// the seller can always withdraw something (should be false before the deadline) 
property seller_wd_early_nonlive {
    Forall xa
    [
      st.winner!=0 && st.balance>0 && closed==false
        ->
      Exists tx [1, st.seller]
      [
        ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}

// the seller can withdraw something in any state (should be false: the contract can be already closed)
property seller_wd_closed_nonlive {
    Forall xa
    [
      st.winner!=0 && st.balance>0 && st.block.number>st.deadline 
        ->
      Exists tx [1, st.seller]
      [
        ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}

// the seller can withdraw something in any state (should be false: if the winner has not been set, the contract balance could be 0)
property seller_wd_nowinner_nonlive {
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

// only the seller can fire the close transaction
property nonseller_wd_nonlive {
    Forall xa
    [
      st.winner!=0
        ->
      Exists tx [1, xa]
      [
        xa != st.seller && ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
      ]
    ]
}


// the extra budget can always be redeemed by the owner
property liquidity_nonlive {
    Forall xa
    [
      closed == true
        ->
      Exists tx [1, xa]
      [
        app_tx_st.balance[st.seller] >= st.balance[st.seller] + st.balance
      ]
    ]
}

// only the seller can increase its balance (should be false: why??)
// property onlyseller_can_gain_nonlive {
//     Forall xa
//     [
//       st.winner!=0 && st.balance>0 && st.block.number>st.deadline && (not closed)
//         ->
//       Exists tx [1, xa]
//       [
//         xa != st.seller && ((app_tx_st.balance[xa] > st.balance[xa]))
//       ]
//     ]
// }

// Deadline can be not passed, but seller can "cheat" by bidding two times (so withdrawing the first bid) 
// property sellerCanWithdraw_live2 {
//     Forall xa
//     [
//       st.winner!=0 && st.balance>0 && closed ==false
//         ->
//       Exists tx [2, st.seller]
//       [
//         ((app_tx_st.balance[st.seller] > st.balance[st.seller]))
//       ]
//     ]
// }
