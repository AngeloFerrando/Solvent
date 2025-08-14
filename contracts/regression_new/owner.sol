
contract C {
    int v;
    address owner;

    constructor(int initial_v) {
        require(msg.sender != this); /* TODO remove */
        v = initial_v;
        owner = msg.sender
    }

    function add(int c) {
        require(msg.sender == owner || c > 0); /* only owner can decrease */
        v = v + c
    }
}


rule P0_true {
    forall addr : address .
    exists f : method .
    exists args : calldataargs .
    << addr : C . f(args) $ 0 >>			
        v == old(v)+1
}
rule P2_true {
    exists addr : address .
    exists f : method .
    exists args : calldataargs .
    << addr : C . f(args) $ 0 >>			
        v == old(v) - 1
}


rule P3_false {
    forall addr : address .
    addr != owner ->
    exists f : method .
    exists args : calldataargs .
    << addr : C . f(args) $ 0 >>			
        v == old(v) - 1
}

rule P4_true {
    forall addr : address .
    forall f : method .
    forall args : calldataargs .
    << addr : C . f(args) $ 0 >>			
        balance[owner] == old(balance[owner])
}


rule P5_false {
    exists addr : address .
    exists f : method .
    exists args : calldataargs .
    << addr : C . f(args) $ 0 >>			
        balance[owner] != old(balance[owner])
}