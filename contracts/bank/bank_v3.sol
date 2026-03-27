// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/bank
// mutation: withdraws must be previously enabled by the owner

contract Bank {
    mapping (address => int) funds;
    address owner;
    bool withdrawalAllowed;

    constructor() {
        owner = msg.sender;
        withdrawalAllowed = false
    }

    function deposit() payable {
        require(msg.value > 0);
        funds[msg.sender] = funds[msg.sender] + msg.value
    }

    function allow_withdraw() {
        require(msg.sender == owner);
        withdrawalAllowed = true
    }

    function withdraw(int amount) {
        require(amount > 0);
        require(amount <= funds[msg.sender]);
        require(withdrawalAllowed);

        funds[msg.sender] = funds[msg.sender] - amount;
        msg.sender.transfer(amount)
    }
}  


// @groundtruth: False
rule Liquidity {
    forall addr : address .
    forall n : int .
    (n >= 0 && n <= funds[addr]) ->
    exists f: method .
    exists args: calldataargs .
    (<< addr : Bank . f(args) $ 0 >>		
            funds[addr] == old(funds[addr]) - n
            &&
            balance[addr] == old(balance[addr] + n)
    )
}

// @groundtruth: True
rule Liquidity_only_user {
    forall addrA : address .
    forall addrB : address .
    forall f: method .
    forall args: calldataargs .
    forall c1 : int .
    (<< addrB : Bank . f(args) $ c1 >>		
            (old(funds[addrA]) > 0 && funds[addrA] == 0) -> addrA == addrB
    )
}

// @groundtruth: True
rule No_frontrun_deposit {
    forall addrA : address .
    forall nA : int .
    forall addrB : address .
    forall f : method .
    forall args : calldataargs .
    forall nB : int .
    exists funds_later_path1 : int .
    exists funds_later_path2 : int .
    (addrA != addrB) ->
    (
        (
        << addrA : Bank . deposit() $ nA >>		
            funds_later_path1 == funds[addrA]
        )
        &&
        (
        << addrB : Bank . f(args) $ nB >>	
            << addrA : Bank . deposit() $ nA >>	
                funds_later_path2 == funds[addrA]
        )
        &&
        funds_later_path1 == funds_later_path2 
    )
}


// @groundtruth: True
rule Additivity {
    forall addr : address .
    forall c1 : int .
    forall c2 : int .
    exists v12_storage : int .
    exists v3_storage : int .
    exists reverted1 : bool .
    exists reverted2 : bool .
    exists reverted3 : bool .
    (c1 >= 0 && c2 >= 0)
    ->
    (
    (<< addr : Bank . deposit() $ c1 >>		
        reverted1 == lastReverted 
          &&
       (<< addr : Bank . deposit() $ c2 >>		
            (
                v12_storage == funds[addr]
                && reverted2 == lastReverted
            )
        )
        )
    &&
    (<< addr : Bank . deposit() $ (c1+c2) >>		
            (v3_storage ==  funds[addr] 
                && reverted3 == lastReverted ))
    &&
    ((!reverted1 && !reverted2) -> (!reverted3 && v12_storage == v3_storage))
    )
}


// @groundtruth: False
rule Reversibility_deposit {
    forall addr : address .
    forall c1 : int .
    exists f: method .
    exists args: calldataargs .
    exists c2 : int .
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . f(args) $ c2 >>		
            //(balance[addr] == old(old(balance[addr])))))
            (funds[addr] == old(old(funds[addr])))))
}

// @groundtruth: True
rule Exists_unique_asset_change {
    forall addrA : address .
    forall msg_value : int .
    forall f : method .
    (
    forall args: calldataargs .
    forall amt: int .
    (
        << addrA : Bank . f(args) $ msg_value >>
        (
            (!lastReverted) 
            ->
            (

                exists addrB1 : address .  
                addrB1 != this
                    ->
                    (
                        balance[addrB1] != old(balance[addrB1])
                            &&
                        forall addrB2 : address .  
                        (( addrB2 != this)
                        ->
                        balance[addrB2] == old(balance[addrB2]))

                    )
            )
        )
    ))
}
