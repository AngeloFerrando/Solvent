contract C { 
    int v; 

    function f() { 
        v=1
    } 
        
    function g() { 
        v=2
    }
}

rule P0a_true {
    forall a: address .
    exists h: method .
        <a:C.f()$0> 
            C.v == 1
}

/*
property p0b_false {
    forall a: address.
    exists h: method.
    exists args : calldataargs. // superfluous?
        <a:C.f()$0> 
            C.v==3
}

property p1_true {
    forall a: address.
        <a:C.f()$0> 
            C.v==1  
        && 
        <a:C.g()$0> 
            C.v == 2
}

property p2a_false {
    exists z: int .
    forall a: address.
        <a:C.f()$0> 
            C.v == z
        && 
        <a:C.g()$0> 
            C.v == z
}


property p2b_true {
    exists z: int .
    forall a: address.
        <a:C.f()$0> 
            C.v == z
        && 
        <a:C.g()$0> 
            C.v == z+1
}


property reversibility_a_false {
    forall a: address.
    forall h1: method.   
    forall args1 : calldataargs. // superfluous?
    exists h2: method.
    exists args2 : calldataargs. // superfluous?
        <a:C.h1()$0> 
            <a:C.h2()$0> 
                C.v == old(old(v))
}


property reversibility_b_true {
    (v = 1 or v = 2) 
        ->
    forall a: address.
    forall h1: method.   
    forall args1 : calldataargs. // superfluous?
    exists h2: method.
    exists args2 : calldataargs. // superfluous?
        <a:C.h1()$0> 
            <a:C.h2()$0> 
                C.v == old(old(v))
}
*/