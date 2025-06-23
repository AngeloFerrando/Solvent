
contract Pricebet {
    int initial_pot;
    address immutable owner;
    address immutable oracle_owner;
    address player;
    int deadline;
    int exchange_rate;
    int oracle_exchange_rate;

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
        require(oracle_exchange_rate == 0); // not yet constructed
        oracle_exchange_rate = init_rate
    }


    // TODO fix different owner for oracle
    // function oracle_set_exchange_rate(int new_rate, int msg_value) public {
    function oracle_set_exchange_rate(int new_rate)  payable {
        if (new_rate > oracle_exchange_rate) {
        //require(msg.value == 1000 * (new_rate / oracle_exchange_rate) + 1000);
        require(msg.value == 1000);
        oracle_exchange_rate = new_rate
        }
        else {
        //require(msg.value == 1000 * (oracle_exchange_rate / new_rate) + 1000 );
        require(msg.value == 1000);
        oracle_exchange_rate = new_rate
        }
    }
}


rule Dummy1 {
    True
}

rule R1 {

    exists bal1 : int .
    << player : Pricebet . win() $0 >> 
            (bal1 == balance[player] 
            &&
            bal1 > old(balance[player]))
    ->
    exists adv : address .
    exists v : int .
    exists qfa : method .
    exists qxa : calldataargs .
    exists bal2 : int .
    << adv : Pricebet . qfa() $ v >>		
    << player : Pricebet . win() $ 0 >>
    bal2 == balance[player] 
    &&
    bal2 < bal1

}