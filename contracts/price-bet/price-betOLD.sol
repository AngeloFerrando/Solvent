
contract Pricebet {
    uint initial_pot;
    address immutable owner;
    address oracle_owner; // immutable TODO
    address player;
    int deadline;
    uint exchange_rate;
    uint oracle_exchange_rate; 
    bool oracle_constructed;
    bool player_has_joined;

    constructor(uint _timeout, uint _exchange_rate) payable {
        require (msg.value > 0);
        require (_exchange_rate > 0);
        initial_pot = msg.value;
        owner = msg.sender;
        // oracle = _oracle;
        deadline = block.number + _timeout;
        exchange_rate = _exchange_rate;
        player_has_joined = false
    }

    function join() payable {
        require(msg.value == initial_pot);
        //require(player == address(0));
        player = msg.sender;
        player_has_joined = true
    }

    function win() {
        require(block.number < deadline);
        require(msg.sender == player);
        require(player_has_joined);

        require(oracle_exchange_rate >= exchange_rate);

        player.transfer(balance)
    }

    function timeout() {
        require(block.number >= deadline);
        owner.transfer(balance)
    }


    
    function oracle_constructor(uint init_rate) {
        require(!oracle_constructed); // not yet constructed
        oracle_exchange_rate = init_rate;
        oracle_constructed = true;
        oracle_owner = msg.sender
    }
    


    // function oracle_set_exchange_rate(int new_rate, int msg_value) public {
    function oracle_set_exchange_rate(uint new_rate)  payable {
        require(msg.sender == oracle_owner);
        if (new_rate > oracle_exchange_rate) {
        //require(msg.value == 1000 * (new_rate / oracle_exchange_rate) + 1000);
        //require(msg.value == 1000);
        oracle_exchange_rate = new_rate
        }
        else {
        //require(msg.value == 1000 * (oracle_exchange_rate / new_rate) + 1000 );
        //require(msg.value == 1000);
        oracle_exchange_rate = new_rate
        }
    }
}

// false
// // False because deadline not yet passed
rule No_Frozen_Funds_false {
    forall a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Pricebet . f(args) $ msgvalue >>
        balance[owner] == old(balance[owner] + balance)		
}

// false
// // False because deadline not yet passed
rule No_Frozen_Funds_owner_false {
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << owner : Pricebet . f(args) $ msgvalue >>
        balance[owner] == old(balance[owner] + balance)		
}

//true up to 5 steps
rule No_Frozen_Funds_after_deadline_true {
    block.number >= deadline ->
    (
        forall a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : Pricebet . f(args) $ msgvalue >>
            balance[owner] == old(balance[owner] + balance)		
    )
}

// true up to 6 steps
rule No_Frozen_Funds_after_deadline_exists_true {
    block.number >= deadline ->
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : Pricebet . f(args) $ msgvalue >>
            balance[owner] == old(balance[owner] + balance)		
    )
}

//  true up to 6 steps
rule No_Frozen_Funds_after_deadline_hint_true {
    block.number >= deadline ->
    (
        forall a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : Pricebet . timeout() $ msgvalue >>
            balance[owner] == old(balance[owner] + balance)		
    )
}

rule No_Frozen_Funds_after_deadline_exists_hint_true {
    block.number >= deadline ->
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : Pricebet . timeout() $ msgvalue >>
            balance[owner] == old(balance[owner] + balance)		
    )
}



// invalid after 2 steps
rule Player_cannot_win_false {
    ! (
            exists bal1 : int .
            (<< player : Pricebet . win() $0 >> 
                (bal1 == balance[player] 
                &&
                bal1 > old(balance[player]))
            )
        )
}

// rule Winning_player_can_be_frontrun_true {
//     (oracle_constructed && oracle_owner != player)
//     ->
//         forall bal1 : int .
//         (
//         (<< player : Pricebet . win() $0 >> 
//             (bal1 == balance[player] 
//             &&
//             bal1 > old(balance[player]))
//         )
//         ->
//             exists adv : address .
//             (
//                 adv != player  
//                 &&
//                 exists v : int .
//                 exists qfa : method .
//                 exists qxa : calldataargs .
//                 exists bal2 : int .
//                 << adv : Pricebet . qfa(qxa) $ v >>		
//                     (
//                     block.number == old(block.number)
//                     &&
//                     << player : Pricebet . win() $ 0 >>
//                         (bal2 == balance[player] 
//                         &&
//                         bal2 < bal1)
//                     )
//             )
//         )
// }

// // bug
// rule Winning_player_can_be_frontrun_by_non_oracleowner_false {
//     (oracle_constructed && oracle_owner != player)
//     ->
//         forall bal1 : int .
//         (
//         (<< player : Pricebet . win() $0 >> 
//             (bal1 == balance[player] 
//             &&
//             bal1 > old(balance[player]))
//         )
//         ->
//             exists adv : address .
//             (
//                 adv != player  && adv != oracle_owner
//                 &&
//                 exists v : int .
//                 exists qfa : method .
//                 exists qxa : calldataargs .
//                 exists bal2 : int .
//                 << adv : Pricebet . qfa(qxa) $ v >>		
//                     (
//                     block.number == old(block.number)
//                     &&
//                     << player : Pricebet . win() $ 0 >>
//                         (bal2 == balance[player] 
//                         &&
//                         bal2 < bal1)
//                     )
//             )
//         )
// }


// // bug
// rule Winning_player_can_be_frontrun_by_anyone_false {
//     forall bal1 : int .
//     ((<< player : Pricebet . win() $0 >> 
//             (bal1 == balance[player] 
//             &&
//             bal1 > old(balance[player])))
//     ->
//     forall adv : address .
//     exists v : int .
//     exists qfa : method .
//     exists qxa : calldataargs .
//     exists bal2 : int .
//     << adv : Pricebet . qfa() $ v >>		
//         << player : Pricebet . win() $ 0 >>
//             (bal2 == balance[player] 
//             &&
//             bal2 < bal1))
// }

// Running example phi1
// if the rate is greater than 100 and the player has joined, then some user can fire some transaction to withdraw the entire pot
// true up to 5 steps
rule Running_example1_true {
    (oracle_exchange_rate >= exchange_rate && player_has_joined)
    -> 
    exists a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Pricebet . f(args) $ msgvalue >>
        balance[a] == old(balance[a] + balance)		
}


rule Running_example2_true {
    exists a1 : address .
    exists a2 : address .
    exists f1 : method .
    exists f2 : method .
    exists args1 : calldataargs .
    exists args2 : calldataargs .
    << a1 : Pricebet . f1(args1) $ 0 >>		
        << a2 : Pricebet . f2(args2) $ 0 >>		
            (balance == 0)
}

// valid k=1
rule Running_example3_Frontrun_simple_true {
    oracle_constructed
    ->
    (
    forall a : address .
    exists b : address .
    exists f : method .
    exists args : calldataargs .
    << b : Pricebet . f(args) $ 0 >>		
        << a : Pricebet . win() $ 0 >>
            lastReverted
    )
}

// valid k=1
rule Running_example3_Frontrun_simple_noOracleOwner_false {
    oracle_constructed
    ->
    (
    forall a : address .
    exists b : address .
    (b != oracle_owner 
    &&
    b != a
    &&
    exists f : method .
    exists args : calldataargs .
    << b : Pricebet . f(args) $ 0 >>		
        block.number == old(block.number)
        &&
        << a : Pricebet . win() $ 0 >>
            lastReverted
    )
    )
}
