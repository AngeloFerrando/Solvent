// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/bank

contract Bank {
    mapping (address => int) funds

    constructor() {
        skip
    }

    function deposit() payable {
        require(msg.value > 0);
        funds[msg.sender] = funds[msg.sender] + msg.value
    }


    function withdraw(int amount) {
        require(amount > 0);
        require(amount <= funds[msg.sender]);

        funds[msg.sender] = funds[msg.sender] - amount;
        msg.sender.transfer(amount)
    }
}  




// rule Test {
//     forall addr : address .
//     forall c1 : int .
//     forall c2 : int .
//     (c1 >= 0 && c2 >= 0)
//     -> (
//     exists v12_storage : int .
//     exists v3_storage : int .
//     (<< addr : Bank . deposit() $ (c1+c2) >>		
//             (v3_storage ==  funds[addr] 
//                 && !lastReverted))
//     //&&
//     //(v12_storage == v3_storage)
//     )
// }


// @groundtruth: True
// valid (k=1)
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

// only excluding the case in which the tx3 reverts is not enough 
// we could have 
//  tx1: deposit(2)
//  tx2: deposit(-1)
//  tx3: deposit(1)
// @groundtruth: False
rule Additivity_AssumpRev3 { 
    forall addr : address .
    forall c1 : int .
    forall c2 : int .
    exists v12_storage : int .
    exists v3_storage : int .
    exists reverted1 : bool .
    exists reverted2 : bool .
    exists reverted3 : bool .
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . deposit() $ c2 >>		
            (
                v12_storage == funds[addr]
                && reverted2 == lastReverted
            )
        )
        && reverted1 == lastReverted
        )
    &&
    (<< addr : Bank . deposit() $ (c1+c2) >>		
            (v3_storage ==  funds[addr] 
                && reverted3 == lastReverted ))
    &&
    (reverted3 || v12_storage == v3_storage)
}

// maybe wrong?
// excluding the case in which either tx1 or tx2 revert is enough (it is implied by tx3 reverting, see Additivity_reverted_implication_false) 
// rule Additivity_true2 {
//     forall addr : address .
//     forall c1 : int .
//     forall c2 : int .
//     exists v12_storage : int .
//     exists v3_storage : int .
//     exists reverted1 : bool .
//     exists reverted2 : bool .
//     exists reverted3 : bool .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . deposit() $ c2 >>		
//             (
//                 v12_storage == funds[addr]
//                 && reverted2 == lastReverted
//             )
//         )
//         && reverted1 == lastReverted
//         )
//     &&
//     (<< addr : Bank . deposit() $ (c1+c2) >>		
//             (v3_storage ==  funds[addr] 
//                 && reverted3 == lastReverted ))
//     &&
//     (reverted1 || reverted2  || v12_storage == v3_storage)
// }

// invalid after 0 steps
// @groundtruth: False
rule Additivity_reverted_implication_false {
    forall addr : address .
    forall c1 : int .
    forall c2 : int .
    exists reverted1 : bool .
    exists reverted2 : bool .
    exists reverted3 : bool .
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . deposit() $ c2 >>		
             reverted2 == lastReverted
        )
        && reverted1 == lastReverted
        )
    &&
    (<< addr : Bank . deposit() $ (c1+c2) >>	
                reverted3 == lastReverted )
    &&
    ((reverted1 || reverted2) == (reverted3) )
}

// maybe wrong?
// @groundtruth: True
rule Additivity_reverted_implication_true {
    forall addr : address .
    forall c1 : int .
    forall c2 : int .
    exists reverted1 : bool .
    exists reverted2 : bool .
    exists reverted3 : bool .
    (<< addr : Bank . deposit() $ c1 >>		
        reverted1 == lastReverted
        &&
       (<< addr : Bank . deposit() $ c2 >>		
             reverted2 == lastReverted
        )
        )
    &&
    (<< addr : Bank . deposit() $ (c1+c2) >>	
                reverted3 == lastReverted )
    &&
    (reverted3 -> (reverted1 || reverted2) )
}



// invalid after 0 steps
// @groundtruth: False
rule Additivity_NoAssumpRev {
    forall c1 : int .
    forall c2 : int .
    exists v12_storage : int .
    exists v3_storage : int .
    forall addr : address .
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . deposit() $ c2 >>		
            (v12_storage == funds[addr])))
    &&
    (<< addr : Bank . deposit() $ (c1+c2+1) >>		
            (v3_storage ==  funds[addr]))
    &&
    (v12_storage == v3_storage)
}

// Valid (k=1)
rule Withdraw_reverses_deposit {
    forall addr : address .
    forall c1 : int .
    c1 > 0 ->
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . withdraw(c1) $ 0 >>		
            (!lastReverted && old(!lastReverted)) ->
              (funds[addr] == old(old(funds[addr])))))
}


// Valid (k=1)
rule BalanceGeq0 {
    forall addr : address .
    balance[addr] >= 0
}

// Valid (k=1)
rule DepositNotRevImplWithNotRev {
    (forall addr : address .
    forall c1 : int .
    c1 > 0 ->
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . withdraw(c1) $ 0 >>		
            (old(!lastReverted) -> !lastReverted) 
              )))
}

// Valid (k=1)
rule DepositNotRevImplWithNotRev_Hint {
    (forall addr : address .
    balance[addr] >= 0)
    ->
    (forall addr : address .
    forall c1 : int .
    c1 > 0 ->
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . withdraw(c1) $ 0 >>		
            (old(!lastReverted) -> !lastReverted) 
              )))
}

// valid (k=1)
// @groundtruth: True
rule Deposit_increase_funds {
    forall addr : address .
    forall c1 : int .
    (<< addr : Bank . deposit() $ c1 >>		
        !lastReverted ->
              (funds[addr] == old(funds[addr])+c1))
}

// valid (k=1)
// @groundtruth: True
rule Withdraw_decrease_funds {
    forall addr : address .
    forall c1 : int .
    (<< addr : Bank . withdraw(c1) $ 0 >>		
        !lastReverted ->
              (funds[addr] == old(funds[addr])-c1))
}


// valid (k=1)
// @groundtruth: True
rule Deposit_monotonicity_ifNotRev {
    forall addr : address .
    forall c1 : int .
    c1 > 0 ->
    (<< addr : Bank . deposit() $ c1 >>		
        !lastReverted ->
              (funds[addr] > old(funds[addr])))
}

// invalid after 0 steps
// @groundtruth: False
rule Deposit_monotonicity {
    forall addr : address .
    forall c1 : int .
    c1 > 0 ->
    (<< addr : Bank . deposit() $ c1 >>		
            (funds[addr] > old(funds[addr])))
}

// valid (k=2)
rule Reversibility_deposit {
    forall addr : address .
    forall c1 : int .
    exists f: method .
    exists args: calldataargs .
    exists c2 : int .
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . f(args) $ c2 >>		
            (funds[addr] == old(old(funds[addr])))))
}





// TODO exists-unique-asset-change
//         "exists-unique-asset-change": "after a non-reverting `deposit` or `withdraw` transaction to the Bank contract, the ETH balance of exactly one account (except the contract's) have changed",

// valid (k=1)
// TODO errore
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
                        (
                        ( addrB2 != this 
                        && addrB2 != addrB1
                        )
                        ->
                        balance[addrB2] == 1+old(balance[addrB2]))
                    )
            )
        )
    ))
}

// valid (k=1)
rule Max_One_asset_change {
    forall addrA : address .
    forall msg_value : int .
    forall f : method .
    (
    forall args: calldataargs .
    //forall amt: int .
    forall addrB : address .  
    addrB != addrA ->
    (
        << addrA : Bank . f(args) $ msg_value >>
        (
            (!lastReverted) 
            ->
            (
                //(balance[addrA] != old(balance[addrA]))
                (balance[addrA] != old(balance[addrA])
                ->
                balance[addrB] == old(balance[addrB])
                )
            )
        )
    ))
}

//valid (k=1)
rule Someone_asset_change {
    forall addrA : address .
    forall msg_value : int .
    forall f : method .
    //(f == withdraw || f == deposit )    ->
    (
    forall args: calldataargs .
    //forall amt: int .
    exists addrB : address .  
    //((f == deposit && msg_value > 0))
    //->
    (
        //<< addrA : Bank . deposit() $ msg_value >>
        //<< addrA : Bank . withdraw(amt) $ msg_value >>
        << addrB : Bank . f(args) $ msg_value >>
        (
            (!lastReverted) 
            ->
            (
                (balance[addrB] != old(balance[addrB]))
                //(funds[addrB] != old(funds[addrB]))
            )
        )
    ))
}

// valid (k=1)
rule Sender_asset_change {
    forall addrA : address .
    forall msg_value : int .
    forall f : method .
    //(f == withdraw || f == deposit )    ->
    (
    forall args: calldataargs .
    //forall amt: int .
    //exists addrB : address .  
    //((f == deposit && msg_value > 0))
    //->
    (
        << addrA : Bank . f(args) $ msg_value >>
        (
            (!lastReverted) 
            ->
            (
                (balance[addrA] != old(balance[addrA]))
                //(funds[addrA] != old(funds[addrA]))
            )
        )
    ))
}

// TODO segnalare
// rule Asdsadsad {
//     forall addrA : address .
//     forall msg_value : int .
//     forall f : method .
//         << addrA : Bank . f(asdsadsad) $ msg_value >>
//         true
// }


// TODO segnalare
// rule WithdrawChangesBalance {
//     forall addrA : address .
//     forall amt: int .
//     // forall pippo : int .
//     // forall msg_value : int .
//     // forall f : method .
//     forall pippo: calldataargs .
//     (
//         << addrA : Bank . withdraw(amt) $ 0 >>
//         (
//             !lastReverted 
//             ->
//             (
//                 (balance[addrA] != old(balance[addrA]))
//                 //(funds[addrA] != old(funds[addrA]))
//             )
//         )
//     )
// }

// @groundtruth: True
rule Liquidity {
    forall addr : address .
    exists f: method .
    exists args: calldataargs .
    exists c1 : int .
    (<< addr : Bank . f(args) $ c1 >>		
            funds[addr] == 0
    )
}

// @groundtruth: True
rule Liquidity_only_user {
    forall addrA : address .
    forall addrB : address .
    exists f: method .
    exists args: calldataargs .
    exists c1 : int .
    (<< addrB : Bank . f(args) $ c1 >>		
            (old(funds[addrA]) > 0 && funds[addrA] == 0) -> addrA == addrB
    )
}


// property deposit_not_revert_liquid {
//     Forall xa
//       [
//         balance[xa]>0 
//           -> 
//         Exists tx [1, xa]
//         [
//           (<tx>funds[xa] == funds[xa] + balance[xa])
//         ]
//       ]
// }


// property withdraw_not_revert_liquid {
//     Forall xa
//       [
//         funds[xa]>0 
//           -> 
//         Exists tx [1, xa]
//         [
//           (<tx>balance[xa] >= balance[xa] + funds[xa])
//         ]
//       ]
// }


