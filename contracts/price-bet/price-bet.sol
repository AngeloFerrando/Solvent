contract Bet {

    bool player_has_joined;
    address owner;
    address oracle;
    address player;
    int rate

    constructor(address oracle_addr, int initial_rate) {
        require(oracle_addr != this);
        owner = msg.sender;
        oracle = oracle_addr; 
        rate = initial_rate 
    }

    function join() {
        require (balance == 2 * msg.value && !player_has_joined) ;
        player = msg.sender ;
        player_has_joined = true 
    }
    function win() {
        require(rate >100);
        require(player_has_joined);
        player.transfer(balance) 
    }

    function set(int x) {
        require (msg.sender == oracle) ;
        rate = x 
    }
}


rule No_Frozen_Funds {
    player_has_joined
    ->
    forall a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Bet . f(args) $ msgvalue >>
        balance[owner] == old(balance[owner] + balance)		
}

// if the rate is greater than 100 and the player has joined, then some user can fire some transaction to withdraw the entire pot
// true up to 5 steps
rule Running_example1_true {
    (rate >= 100 && player_has_joined)
    -> 
    exists a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Bet . f(args) $ msgvalue >>
        balance[a] == old(balance[a] + balance)		
}

rule Running_example1_plus1_false {
    (rate >= 100 && player_has_joined)
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



rule Running_example3_Frontrun_simple_true {
    (player_has_joined)
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

rule Running_example3_Frontrun_simple_trace_true {
    (player_has_joined)
    ->
    (
    forall a : address .
    << oracle : Pricebet . set(50) $ 0 >>		
        << a : Pricebet . win() $ 0 >>
            lastReverted
    )
}


rule Running_example3_Frontrun_simple_false {
    (player_has_joined)
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

