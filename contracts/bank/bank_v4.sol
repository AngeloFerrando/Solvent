// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/bank
// mutation: in deposit the contract subtracts 1 from the deposited amount

contract Bank {
    mapping (address => int) funds;
    address owner

    constructor() {
        owner = msg.sender
    }

    function deposit() payable {
        require(msg.value > 0);
        funds[msg.sender] = funds[msg.sender] + msg.value 
    }


    function withdraw(int amount) {
        require(amount > 0);
        require(amount <= funds[msg.sender]);

        funds[msg.sender] = funds[msg.sender] - amount;
        msg.sender.transfer(amount - 1);
        owner.transfer(1)
    }
}  


rule Additivity_true {
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


rule Reversibility_deposit_true {
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

rule Exists_unique_asset_change {
    forall addrA : address .
    forall msg_value : int .
    forall f : method .
    (
    forall args: calldataargs .
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
                        (( addrB2 != this && addrB2 != addrB1)
                        ->
                        balance[addrB2] == old(balance[addrB2]))
                    )
            )
        )
    ))
}