contract Mapping2 {
    mapping (address => int) m;

    function foo() {
        m[msg.sender] = 10
    }

    function faa() {
        require(m[msg.sender] > 10)
    }

    function fee() {
        m[msg.sender] = m[msg.sender] + 1
    }
}  