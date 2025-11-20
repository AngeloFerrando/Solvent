contract Mapping1 {
    mapping (address => int) m;

    function foo() {
        m[msg.sender] = m[msg.sender] + 1
    }
}  

rule P1_true {
    forall a : address .
    exists h : method .
        << a : Mapping1 . h() $ 0 >> 
            m[a] == old(m[a]) + 1
}

rule P1b_true {
    forall a : address .
    exists h : method .
        << a : Mapping1 . h() $ 0 >> 
            m[a] > old(m[a]) 
}


rule P2_false {
    forall a : address .
    exists h : method .
        << a : Mapping1 . h() $ 0 >> 
            m[a] == old(m[a]) + 2
}


rule P3_true {
    forall a : address .
    exists h1 : method .
    exists h2 : method .
        << a : Mapping1 . h1() $ 0 >> 
          << a : Mapping1 . h2() $ 0 >> 
              m[a] == old(old(m[a])) + 2
}
