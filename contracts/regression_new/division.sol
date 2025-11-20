
contract Division {
    int v;

    constructor(int initial_v) {
        v = initial_v
    }

    
    function divide(int c) {
        /*require(c>0);*/
        v = c  / v
    }

    function multiply(int d) {
        v = v  * d
    }
}


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
}



rule P2_false {
    forall c1 : int .
    exists c3 : int .
    exists v1_storage : int .
    exists v3_storage : int .
    forall addr : address .
    (<< addr : Division . multiply(c1) $ 0 >>		
        (v1_storage == v))
    &&
    (<< addr : Division . multiply(c3) $ 0 >>		
        (v3_storage == v))
    &&
    (v1_storage + 1 == v3_storage)
}

