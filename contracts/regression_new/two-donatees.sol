
contract TwoDonatee {
    address p1;
    address p2;
    bool started;

    constructor(int initial_v) {
        p1 = msg.sender;
        started = false
    }

    function join() payable {
        require(msg.sender != p1);
        require(!started);
        p2 = msg.sender;
        started = true
    }

    
    // translates `donatee` as int in kind2, which triggers an error 
    // error: Cannot unify type int with inferred type enum { aTwoDonatee, a1, a2 } 
    /*
    function donate(address donatee) payable { 
        require(started);
        //donatee.transfer(msg.value);
        if (donatee == p1) {
            p1.transfer(msg.value)
        }
        else {
            p2.transfer(msg.value)
        }
    }*/
    
    function donate(int donatee_index) payable {
        require(started);
        require(donatee_index == 1 || donatee_index == 2);
        if (donatee_index == 1) {
            p1.transfer(msg.value)
        }
        else {
            p2.transfer(msg.value)
        }
    }


}

rule P1_false {
    started ->
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : TwoDonatee . f(args) $ msgvalue >>
            balance[p1] > old(balance[p1])	
    )	
}

// kind2 returns unknown
rule P2_true {
    (started && balance[p2] > 0) ->
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : TwoDonatee . f(args) $ msgvalue >>
            balance[p1] > old(balance[p1])	
    )	
}


rule P3_false {
    (started && balance[this] > 0) ->
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : TwoDonatee . f(args) $ msgvalue >>
            balance[p1] > old(balance[p1])	
    )	
}



// kind2 returns unknown
rule P4_true {
    (started && balance[p2] > 0 && balance[this] > 0) ->
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : TwoDonatee . f(args) $ msgvalue >>
            balance[p1] > old(balance[p1])	
    )	
}


rule P2b_true {
    (started && balance[p2] > 0) ->
    (   
        << p2 : TwoDonatee . donate(1) $ 1 >>
            balance[p1] > old(balance[p1])	
    )	
}

rule P5_true {
    (started && balance[p2] == 1 && balance[this] == 1 && p1 != p2) ->
    (
        << p2 : TwoDonatee . donate(1) $ 1 >>
            balance[p1] > old(balance[p1])	
    )	
}

rule P5_false {
    (started && balance[p2] == 1 && balance[this] == 1 && p1 != p2) ->
    (
        << p2 : TwoDonatee . donate(1) $ 1 >>
            balance[p1] <= old(balance[p1])	
    )	
}





rule P2_false {
    started -> 
    (
        exists a : address .
        a != p1 &&
        (
            exists f : method .
            exists args : calldataargs .    
            exists msgvalue : int .    
            << a : TwoDonatee . f(args) $ msgvalue >>
                balance[p1] < old(balance[p1])	
        )	
    )
}



rule P2b_false {
    started -> 
    (
        exists a : address .
        a != p1 &&
        (
            exists donate_arg : int .    
            exists msgvalue : int .    
            << a : TwoDonatee . donate(0) $ msgvalue >>
                balance[p1] < old(balance[p1])	
        )	
    )
}

rule P2c_false {
    started -> 
    (
        exists donate_arg : int .    
        exists msgvalue : int .    
        << p2 : TwoDonatee . donate(0) $ msgvalue >>
            balance[p1] < old(balance[p1])	
    )
}


rule P2d_true {
    started -> 
    (
        << p2 : TwoDonatee . donate(0) $ 0 >>
            balance[p1] >= old(balance[p1])	
    )
}

rule P2d_false {
    started -> 
    (
        << p2 : TwoDonatee . donate(0) $ 0 >>
            balance[p1] < old(balance[p1])	
    )
}

rule P3b_false {
    started -> 
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : TwoDonatee . f(args) $ msgvalue >>
            balance[p1] < old(balance[p1])		
    )
}

// kind2 returns unknown
rule P3c_true {
    (started && balance[p1] > 0) -> 
    (
        exists a : address .
        exists f : method .
        exists args : calldataargs .    
        exists msgvalue : int .    
        << a : TwoDonatee . f(args) $ msgvalue >>
            balance[p1] < old(balance[p1])		
    )
}
