
contract Division {
    int v1;
    int v2;

    constructor(int initial_v1, int initial_v2) {
        v1 = initial_v1;
        v2 = initial_v2
    }

    
    function divide(int c) {
        /*require(c>0);*/
        v1 = v1  / v2
    }

    function multiply(int d) {
        v1 = v1 * v2 * d
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
    (<< addr : Division . multiply(c1) $ 0 >>		
       (<< addr : Division . multiply(c2) $ 0 >>		
            (v12_storage == v)))
    &&
    (<< addr : Division . multiply(c3) $ 0 >>		
            (v3_storage == v))
    &&
    (v12_storage == v3_storage)
}*/



rule P2_false {
    forall c1 : int .
    exists c3 : int .
    exists v1_storage : int .
    exists v3_storage : int .
    forall addr : address .
    (<< addr : Division . multiply(c1) $ 0 >>		
        (v1_storage == v1))
    &&
    (<< addr : Division . multiply(c3) $ 0 >>		
        (v3_storage == v1))
    &&
    (v1_storage + 1 == v3_storage)
}

