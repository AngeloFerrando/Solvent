
contract Additivity {
    int v;

    constructor(int initial_v) {
        v = initial_v
    }

    function add(int c) {
        v = v + c
    }
}
/*
rule P1_true {
    forall c1 : int .
    forall c2 : int .
    exists c3 : int .
    exists v12_storage : int .
    exists v3_storage : int .
    forall addr : address .
    (<< addr : Addittivity . add(c1) $ 0 >>		
       (<< addr : Addittivity . add(c2) $ 0 >>		
            (v12_storage == v)))
    &&
    (<< addr : Addittivity . add(c3) $ 0 >>		
            (v3_storage == v))
    &&
    (v12_storage == v3_storage)
}



rule P2_false {
    forall c1 : int .
    forall c2 : int .
    forall c3 : int .
    exists v12_storage : int .
    exists v3_storage : int .
    forall addr : address .
    (<< addr : Addittivity . add(c1) $ 0 >>		
       (<< addr : Addittivity . add(c2) $ 0 >>		
            (v12_storage == v)))
    &&
    (<< addr : Addittivity . add(c3) $ 0 >>		
            (v3_storage == v))
    &&
    (v12_storage == v3_storage)
}*/

/*
rule P_signature_error {
    forall v1 : int .
    forall addr : address .
    (<< addr : Addittivity . add() $ 0 >>		
            true)
}
*/


/*
rule P3_true {
    forall addr : address .
    << addr : Addittivity . add(2) $ 0 >>		
        v == old(v)
}


rule P4_false {
    forall addr : address .
    << addr : Addittivity . add() $ 0 >>		
        v == old(v)+3
}
*/
/*
rule P5_true {
    forall addr : address .
    << addr : Addittivity . add(v) $ 0 >>		
        v == 2*old(v)
}

rule P6_false {
    forall addr : address .
    << addr : Addittivity . add(v) $ 0 >>		
        v == 3*old(v)
}
*/

rule P7_true {
    forall addr : address .
    << addr : Addittivity . add(1) $ 0 >>		
    << addr : Addittivity . add(v) $ 0 >>		
        v == 2*(old(old(v))+1)
}


rule P8_false {
    forall addr : address .
    << addr : Addittivity . add(1) $ 0 >>		
    << addr : Addittivity . add(v) $ 0 >>		
        v == 2*old(old(v)) +1
}


rule P9_true {
    forall addr : address .
    << addr : Addittivity . add(v) $ 0 >>		
    << addr : Addittivity . add(1) $ 0 >>		
        v == 2*old(old(v)) +1
}


rule P10_false {
    forall addr : address .
    << addr : Addittivity . add(v) $ 0 >>		
    << addr : Addittivity . add(1) $ 0 >>		
        v == 2*(old(old(v))+1)
}
