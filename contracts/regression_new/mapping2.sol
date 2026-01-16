contract Mapping2 {
    mapping (address => int) m;
    address owner; 

    constructor() {
        owner = msg.sender
    }

    function foo() {
        m[msg.sender] = 10
    }

    function faa() {
        require(m[msg.sender] > 10)
    }

    function fee() {
        m[msg.sender] = m[msg.sender] + 1
    }

    function fii() {
        require(m[owner] > m[msg.sender])
    }
}  



rule P1_true {
    forall a : address .
    exists h : method .
        << a : Mapping2 . h() $ 0 >> 
            m[a] == 10
}

