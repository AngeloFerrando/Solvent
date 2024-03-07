contract PaymentSplitter {
	mapping (address => uint) shares
	int totalShares
    mapping (address => uint) released
	int totalReleased 
    address owner
    int state

    constructor(address o) {
        shares = emptymap;
        released = emptymap;
        owner = o;
        totalShares = 0;
        totalReleased = 0;
        state = 0
    }

    function addShares(p, s) {
        require(msg.sender == owner);
        require(state == 0);
        shares[p] += s;
        totalShares += s
    }

    function finalizeShares() {
        require(msg.sender == owner);
        require(state == 0);
        state = 1
    }

    function receive() payable {
        skip
    } 

    function release(a) { 
        require(shares[a] > 0);
        require(state == 1);
    
        totalReceived = balance() + totalReleased;
        payment = (totalReceived * shares[a]) / totalShares - released[a];
        if (payment != 0) {
            totalReleased += payment;
                released[account] += payment;
            a!payment;
        }
    }
}
