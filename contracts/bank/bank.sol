// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/bank

contract Bank {
    mapping (address => int) funds

    constructor() {
        skip
    }

    function deposit() payable {
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



// rule Additivity_true {
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
//     (reverted3 || reverted2 || reverted1 || v12_storage == v3_storage)
// }

// only excluding the case in which the tx3 reverts is not enough 
// we could have 
//  tx1: deposit(2)
//  tx2: deposit(-1)
//  tx3: deposit(1)
// rule Additivity_false1 { 
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
//     (reverted3 || v12_storage == v3_storage)
// }

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


// rule Additivity_reverted_implication_false {
//     forall addr : address .
//     forall c1 : int .
//     forall c2 : int .
//     exists reverted1 : bool .
//     exists reverted2 : bool .
//     exists reverted3 : bool .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . deposit() $ c2 >>		
//              reverted2 == lastReverted
//         )
//         && reverted1 == lastReverted
//         )
//     &&
//     (<< addr : Bank . deposit() $ (c1+c2) >>	
//                 reverted3 == lastReverted )
//     &&
//     ((reverted1 || reverted2) == (reverted3) )
// }


// rule Additivity_reverted_implication_true {
//     forall addr : address .
//     forall c1 : int .
//     forall c2 : int .
//     exists reverted1 : bool .
//     exists reverted2 : bool .
//     exists reverted3 : bool .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . deposit() $ c2 >>		
//              reverted2 == lastReverted
//         )
//         && reverted1 == lastReverted
//         )
//     &&
//     (<< addr : Bank . deposit() $ (c1+c2) >>	
//                 reverted3 == lastReverted )
//     &&
//     (reverted3 -> (reverted1 || reverted2) )
// }

// rule Additivity_false {
//     forall c1 : int .
//     forall c2 : int .
//     exists v12_storage : int .
//     exists v3_storage : int .
//     forall addr : address .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . deposit() $ c2 >>		
//             (v12_storage == funds[addr])))
//     &&
//     (<< addr : Bank . deposit() $ (c1+c2+1) >>		
//             (v3_storage ==  funds[addr]))
//     &&
//     (v12_storage == v3_storage)
// }

rule Withdraw_reverse_deposit {
    forall addr : address .
    forall c1 : int .
    c1 > 0 ->
    (<< addr : Bank . deposit() $ c1 >>		
       (<< addr : Bank . withdraw(c1) $ 0 >>		
            (!lastReverted && old(!lastReverted)) ->
              (funds[addr] == old(old(funds[addr])))))
}



// rule Deposit_increase_funds_true {
//     forall addr : address .
//     forall c1 : int .
//     (<< addr : Bank . deposit() $ c1 >>		
//         !lastReverted ->
//               (funds[addr] == old(funds[addr])+c1))
// }

// rule Withdraw_decrease_funds_true {
//     forall addr : address .
//     forall c1 : int .
//     (<< addr : Bank . withdraw(c1) $ 0 >>		
//         !lastReverted ->
//               (funds[addr] == old(funds[addr])-c1))
// }


// rule Deposit_monotonicity_true {
//     forall addr : address .
//     forall c1 : int .
//     c1 > 0 ->
//     (<< addr : Bank . deposit() $ c1 >>		
//         !lastReverted ->
//               (funds[addr] > old(funds[addr])))
// }

// rule Deposit_monotonicity_false {
//     forall addr : address .
//     forall c1 : int .
//     c1 > 0 ->
//     (<< addr : Bank . deposit() $ c1 >>		
//             (funds[addr] > old(funds[addr])))
// }


// rule Reversibility_deposit {
//     forall addr : address .
//     forall c1 : int .
//     exists f: method .
//     exists args: calldataargs .
//     exists c2 : int .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . f(args) $ c2 >>		
//             (funds[addr] == old(old(funds[addr])))))
// }








// rule Liquidity {
//     forall addr : address .
//     exists f: method .
//     exists args: calldataargs .
//     exists c1 : int .
//     (<< addr : Bank . f(args) $ c1 >>		
//             funds[addr] == 0
//     )
// }

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