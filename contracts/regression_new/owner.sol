
contract C {
    int v;
    address owner;

    constructor(int initial_v) {
        v = initial_v;
        owner = msg.sender
    }

    function add(int c) {
        require(msg.sender == owner || c > 0); /* only owner can decrease */
        v = v + c
    }
}


rule P1_true {
    forall addr : address .
    exists f : method .
    << addr : C . f() $ 0 >>			
        v == old(v)+1
}


rule P1_false {
    forall addr : address .
    exists f : method .
    << addr : C . f() $ 0 >>			
        v == old(v) - 1
}


rule P2_true {
    exists addr : address .
    exists f : method .
    << addr : C . f() $ 0 >>			
        v == old(v) - 1
}



rule P3_false {
    forall addr : address .
    addr != owner ->
    exists f : method .
    << addr : C . f() $ 0 >>			
        v == old(v) - 1
}
