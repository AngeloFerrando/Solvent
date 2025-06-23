
contract IfRequire {
    int v;

    constructor(int initial_v) payable {
        require (msg.value > 0);
        v = msg.value
    }

    function set_v(int new_v) payable {
        if (new_v > 10) {
            require(msg.value == 100);
            v = new_v
        }
        else {
            require(msg.value == 1);
            v = new_v
        }
        //v = new_v
    }
}


rule Dummy1 {
    True
}


rule R1 {
    forall v1 : int .
    forall addr : address .
    exists qfa : method .
    exists qxa : calldataargs .
    exists msgvalue : int .
    << addr : IfRequire . qfa() $ msgvalue >>		
    v == v1
}


rule R2 {
    forall v1 : int .
    forall addr : address .
    balance[addr] > 100
    ->
    exists qfa : method .
    exists qxa : calldataargs .
    exists msgvalue : int .
    << addr : IfRequire . qfa() $ msgvalue >>		
    v == v1
}