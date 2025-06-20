contract Mapping1 {
    mapping (address => int) m;

    function foo() {
        m[msg.sender] = m[msg.sender] + 1
    }
}  

/*
property liquid1 {
    Forall xa
      [
        true 
          -> 
        Exists tx [1, xa]
        [
          (<tx>m[xa] == m[xa] + 1)
        ]
      ]
}
*/

rule P1 {
    forall a : address .
    exists h : method .
        << a : Mapping1 . h() $ 0 >> 
            m[a] == m[a] + 1
}