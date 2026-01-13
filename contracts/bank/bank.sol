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





// rule Additivity {
//     forall c1 : int .
//     forall c2 : int .
//     exists v12_storage : int .
//     exists v3_storage : int .
//     exists v : int .
//     forall addr : address .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . deposit() $ c2 >>		
//             (v12_storage == v)))
//     &&
//     (<< addr : Bank . deposit() $ (c1+c2) >>		
//             (v3_storage == v))
//     &&
//     (v12_storage == v3_storage)
// }

// rule Additivity_existsc3 {
//     forall c1 : int .
//     forall c2 : int .
//     exists c3 : int .
//     exists v12_storage : int .
//     exists v3_storage : int .
//     exists v : int .
//     forall addr : address .
//     (<< addr : Bank . deposit() $ c1 >>		
//        (<< addr : Bank . deposit() $ c2 >>		
//             (v12_storage == v)))
//     &&
//     (<< addr : Bank . deposit() $ c3 >>		
//             (v3_storage == v))
//     &&
//     (v12_storage == v3_storage)
// }


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