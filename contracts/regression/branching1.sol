contract C { 
    int v; 

    function f() { 
        v=1
    } 
        
    function g() { 
        v=2
    }
}

/*rule P0a_true {
    forall a : address .
    exists h : method .
        << a : C . h() $ 0 >> 
            v == 1
}*/

rule P0b_false {
    forall a: address .
    exists h: method .
        << a : C . f() $ 0 >> 
            v==3
}