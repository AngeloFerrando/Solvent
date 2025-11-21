
contract Pricebet {
    int initial_pot;
    address immutable owner;
    address oracle_owner; // immutable TODO
    address player;
    int deadline;
    int exchange_rate;
    int oracle_exchange_rate; 
    bool oracle_constructed;

    constructor(int _timeout, int _exchange_rate) payable {
        require (msg.value > 0);
        initial_pot = msg.value;
        owner = msg.sender;
        // oracle = _oracle;
        deadline = block.number + _timeout;
        exchange_rate = _exchange_rate
    }

    function join() payable {
        require(msg.value == initial_pot);
        //require(player == address(0));
        player = msg.sender
    }

    function win() {
        require(block.number < deadline);
        require(msg.sender == player);

        require(oracle_exchange_rate >= exchange_rate);

        player.transfer(balance)
    }

    function timeout() {
        require(block.number >= deadline);
        owner.transfer(balance)
    }


    
    function oracle_constructor(int init_rate) {
        require(!oracle_constructed); // not yet constructed
        oracle_exchange_rate = init_rate;
        oracle_constructed = true;
        oracle_owner = msg.sender
    }
    


    // TODO fix different owner for oracle
    // function oracle_set_exchange_rate(int new_rate, int msg_value) public {
    function oracle_set_exchange_rate(int new_rate)  payable {
        require(msg.sender == oracle_owner);
        if (new_rate > oracle_exchange_rate) {
        require(msg.value == 1000 * (new_rate / oracle_exchange_rate) + 1000);
        //require(msg.value == 1000);
        oracle_exchange_rate = new_rate
        }
        else {
        require(msg.value == 1000 * (oracle_exchange_rate / new_rate) + 1000 );
        //require(msg.value == 1000);
        oracle_exchange_rate = new_rate
        }
    }
}


/*
rule No_Frozen_Funds_false {
    forall a : address .
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << a : Pricebet . f(args) $ msgvalue >>
        balance[owner] == old(balance[owner] + balance)		
}

rule No_Frozen_Funds_owner_false {
    exists f : method .
    exists args : calldataargs .    
    exists msgvalue : int .    
    << owner : Pricebet . f(args) $ msgvalue >>
        balance[owner] == old(balance[owner] + balance)		
}
*/

// rule No_Frozen_Funds_after_deadline_true {
//     block.number >= deadline ->
//     (
//         forall a : address .
//         exists f : method .
//         exists args : calldataargs .    
//         exists msgvalue : int .    
//         << a : Pricebet . f(args) $ msgvalue >>
//             balance[owner] == old(balance[owner] + balance)		
//     )
// }

// rule No_Frozen_Funds_after_deadline_exists_true {
//     block.number >= deadline ->
//     (
//         exists a : address .
//         exists f : method .
//         exists args : calldataargs .    
//         exists msgvalue : int .    
//         << a : Pricebet . f(args) $ msgvalue >>
//             balance[owner] == old(balance[owner] + balance)		
//     )
// }

// rule No_Frozen_Funds_after_deadline_hint_true {
//     block.number >= deadline ->
//     (
//         forall a : address .
//         exists f : method .
//         exists args : calldataargs .    
//         exists msgvalue : int .    
//         << a : Pricebet . timeout() $ msgvalue >>
//             balance[owner] == old(balance[owner] + balance)		
//     )
// }

// rule No_Frozen_Funds_after_deadline_exists_hint_true {
//     block.number >= deadline ->
//     (
//         exists a : address .
//         exists f : method .
//         exists args : calldataargs .    
//         exists msgvalue : int .    
//         << a : Pricebet . timeout() $ msgvalue >>
//             balance[owner] == old(balance[owner] + balance)		
//     )
// }





rule Winning_player_can_be_frontrun {
    forall bal1 : int .
    ((<< player : Pricebet . win() $0 >> 
            (bal1 == balance[player] 
            &&
            bal1 > old(balance[player])))
    ->
    exists adv : address .
    exists v : int .
    exists qfa : method .
    exists qxa : calldataargs .
    exists bal2 : int .
    << adv : Pricebet . qfa() $ v >>		
        << player : Pricebet . win() $ 0 >>
            (bal2 == balance[player] 
            &&
            bal2 < bal1))
}


