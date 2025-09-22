
contract TwoDonatee {
    address p1;
    address p2;
    bool started;
    int c;

    constructor(int initial_v) {
        p1 = msg.sender;
        started = false;
        c = 0
    }


    function join() payable {
        require(msg.sender != p1);
        require(!started);
        p2 = msg.sender;
        started = true
    }

    function donate(int donatee_index) payable {
        p1.transfer(msg.value)
    }

    //function dummy(1) { // ok
    function dummy() {  // "Function donate requires 0 arguments, but 1 are given (line 39, column 8)"
        skip
    }

}

rule P5_true {
    (started && balance[p2] == 1 && balance[this] == 1) ->
    (
        << p2 : TwoDonatee . donate(1) $ 1 >>
            balance[p1] > old(balance[p1])	
    )	
}