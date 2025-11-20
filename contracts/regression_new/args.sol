contract C { 
    int v; 

    function add(int x) { 
        require(x >= 0);
        v=v+x
    } 
        
    function set(int y) { 
        v=y
    }
}

rule P0_false {
    exists a : address .
    exists arg : calldataargs .
        << a : C . add(0) $ 0 >> 
            v == -1
}

rule P1_true {
    forall a : address .
    forall v_after : int .
    exists h : method .
    exists arg : calldataargs .
        << a : C . h(arg) $ 0 >> 
            v == v_after
}
// false if v_after < 0
rule P2_false {
    forall a : address .
    forall v_after : int .
    forall h : method .
    exists arg : calldataargs .
        << a : C . h(arg) $ 0 >> 
            v == v_after
}


rule P3a_true {
    forall a : address .
    forall v_after : int .
    v_after >= v ->
        (
        forall h : method .
        exists arg : calldataargs .
            << a : C . h(arg) $ 0 >> 
                v == v_after)
}


rule P3b_false {
    forall a : address .
    forall v_after : int .
    v_after > 0 ->
        (
        forall h : method .
        exists arg : calldataargs .
            << a : C . h(arg) $ 0 >> 
                v == v_after)
}


rule P3c_true {
    forall a : address .
    forall v_after : int .
    v_after * v_after * v_after >= v * v * v ->
        (
        forall h : method .
        exists arg : calldataargs .
            << a : C . h(arg) $ 0 >> 
                v == v_after)
}


rule P4_false {
    forall a : address .
    forall v_after : int .
    forall h : method .
    forall arg : calldataargs .
        << a : C . h(arg) $ 0 >> 
            v == v_after
}


rule P5_true {
    forall a : address .
    exists h : method .
    forall arg : calldataargs .
        << a : C . h(arg) $ 0 >> 
            v >= old(v)
}


rule P6_false {
    forall a : address .
    forall h : method .
    forall arg : calldataargs .
        << a : C . h(arg) $ 0 >> 
            v >= old(v)
}


rule P7_true {
    forall a : address .
    forall h : method .
    h != set ->
        forall arg : calldataargs .
            << a : C . h(arg) $ 0 >> 
                v >= old(v)
}

