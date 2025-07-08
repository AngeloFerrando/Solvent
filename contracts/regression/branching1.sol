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
    forall a : address .
    exists h : method .
        << a : C . h() $ 0 >> 
            v == 1
}



rule P0b_false {
    forall a : address .
    exists h : method .
        << a : C . f() $ 0 >> 
            v==3
}



rule P1_true {
    forall a : address .
        (<< a : C . f() $ 0 >> 
            v == 1)  
        && 
        (<< a : C . g() $ 0 >> 
            v == 2)
}



rule P2a_false {
    exists z : int .
    forall a : address .
        (<<a : C . f() $ 0>> 
            v == z)
        && 
        (<<a : C . g() $ 0>> 
            v == z)
}



rule P2b_true {
    exists z : int .
    forall a : address .
        (<< a : C . f() $ 0 >> 
            v == z)
        && 
        (<< a : C . g() $ 0 >> 
            v == z+1)
}


rule Reversibility_a_false {
    forall a : address .
    forall h1 : method .   
    exists h2 : method .
        << a : C . h1() $ 0 >> 
            << a : C . h2() $ 0 >> 
                v == old(old(v))
}


rule Reversibility_b_true {
    (v == 1 or v == 2) 
        ->
    (
        forall a : address .
        forall h1 : method .
        exists h2 : method .
            << a : C . h1() $ 0 >> 
                << a : C . h2() $ 0 >> 
                    v == old(old(v))
    )
}
