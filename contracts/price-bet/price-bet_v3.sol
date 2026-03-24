contract Bet {

    bool player_has_joined;
    address owner;
    address oracle;
    address player;
    int rate;
    bool player_won

    constructor(address oracle_addr, int initial_rate) payable {
        require(oracle_addr != this);
        owner = msg.sender;
        oracle = oracle_addr; 
        rate = initial_rate;
        player_has_joined = false;
        player_won = false
    }

    function join() payable {
        require (balance == 2 * msg.value && !player_has_joined) ;
        player = msg.sender ;
        player_has_joined = true 
    }
    function win() {
        require(player_won);
        player.transfer(balance) 
    }
    function set() {
        require (msg.sender == oracle) ;
        player_won = true
    }

    // bugged
    // function set(int x) {
    //     require (msg.sender == oracle) ;
    //     rate = x ;
    //     if (rate > 100 && player_has_joined) {
    //         player_won = true
    //     } else { 
    //         skip 
    //     }
    // }
}


rule No_Frozen_Funds_false {
    player_has_joined
    ->
    forall a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Bet . f(args) $ msgvalue >>
        balance[owner] == old(balance[owner] + balance)		
}

rule Running_example1_false {
    (rate > 100 && player_has_joined)
    -> 
    exists a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Bet . f(args) $ msgvalue >>
        balance[a] == old(balance[a] + balance)		
}

rule Running_example1_plus1_false {
    (rate > 100 && player_has_joined)
    -> 
    exists a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Bet . f(args) $ msgvalue >>
        balance[a] == old(balance[a] + balance) + 1		
}

rule Running_example2_true {
    player_has_joined
    ->
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

rule Running_example2_baleq1_false {
    player_has_joined
    ->
    exists a1 : address .
    exists a2 : address .
    exists f1 : method .
    exists f2 : method .
    exists args1 : calldataargs .
    exists args2 : calldataargs .
    << a1 : Pricebet . f1(args1) $ 0 >>		
        << a2 : Pricebet . f2(args2) $ 0 >>		
            (balance == 1)
}



rule Running_example3_Frontrun_simple_false {
    (player_won)
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

// rule Running_example3_Frontrun_simple_trace_false {
//     (player_has_joined)
//     ->
//     (
//     forall a : address .
//     << oracle : Pricebet . set(50) $ 0 >>		
//         << a : Pricebet . win() $ 0 >>
//             lastReverted
//     )
// }


rule Running_example3_Frontrun_notByOracle_simple_false {
    (player_won)
    ->
    (
    forall a : address .
    exists b : address .
    b != oracle &&
    exists f : method .
    exists args : calldataargs .
    << b : Pricebet . f(args) $ 0 >>		
        << a : Pricebet . win() $ 0 >>
            lastReverted
    )
}


rule Running_example3_Frontrun_notByOracle_noblocknumIncrease_false {
    (player_won)
    ->
    (
    forall a : address .
    exists b : address .
    b != oracle &&
    exists f : method .
    exists args : calldataargs .
    << b : Pricebet . f(args) $ 0 >>		
        block.number == old(block.number) &&
        << a : Pricebet . win() $ 0 >>
            lastReverted
    )
}
