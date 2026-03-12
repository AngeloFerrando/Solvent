// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/vault

contract Vault {
    address owner;
    address recovery;
    uint wait_time;

    address receiver;
    uint request_time;
    uint amount;
    int state;
    // 0 = IDLE
    // 1 = REQ
   
    constructor (address recovery_, int wait_time_) payable {
    	require(msg.sender != recovery_);
        owner = msg.sender;
        recovery = recovery_;
        wait_time = wait_time_;
        state = 0 // IDLE
    }

    // receive() external payable { }

    function withdraw(address receiver_, int amount_) {
        require(state == 0); // IDLE
        require(amount_ <= balance);
        require(msg.sender == owner);

        request_time = block.number;
        amount = amount_;
        receiver = receiver_;
        state = 1 // REQ
    }

    function finalize() {
        require(state == 1); // REQ
        require(block.number >= request_time + wait_time);
        require(msg.sender == owner);

        state = 0; // IDLE	
        receiver.transfer(amount)
    }

    function cancel() {
        require(state == 1); // REQ
        require(msg.sender == recovery);
        state = 0 // IDLE
    }
}

// rule Dummy_true {
//     (state == 0 && balance == 0) ->
//     (
//     exists recipient: address .
//     true
//     )
// }

// rule Dummy_false {
//     (state == 0 && balance == 0) ->
//     (
//     exists recipient: address .
//     state ==1
//     )
// }


// rule Tx_tx_assets_transfer_trace_false1 {
//     (state == 0 && balance == 0) ->
//     (
//     exists recipient: address .
//     (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
//         //block.number >= request_time + wait_time
//         //true
//         //->
//         << owner : Vault . finalize() $ 0 >>		
//               //(balance[recipient] ==  old(old(balance[recipient]))  )
//               (balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
//               //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }

// rule Tx_tx_assets_transfer_trace_false2 {
//     (state == 0 && balance == 0) ->
//     (
//     exists recipient: address .
//     (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
//         //block.number >= request_time + wait_time
//         //true
//         //->
//         << owner : Vault . finalize() $ 0 >>		
//               //(balance[recipient] ==  old(old(balance[recipient]))  )
//               //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
//               (balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }

// rule Tx_tx_assets_transfer_trace_true {
//     (state == 0 && balance > 0) ->
//     (
//     exists recipient: address .
//     (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
//         //block.number >= request_time + wait_time
//         //true
//         //->
//         << owner : Vault . finalize() $ 0 >>		
//               (balance[recipient] ==  old(old(balance[recipient]))  )
//               //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
//               //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }

// not working (issue with block number increasing?)
rule Tx_tx_assets_transfer_trace_balance_true {
    (state == 0 && balance > 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
        block.number >= request_time + wait_time
        //true
        ->
        << owner : Vault . finalize() $ 0 >>		
              (balance[recipient] ==  old(old(balance[recipient])) +  old(old(balance))  )
              //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
              //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
    ))
}

// rule Tx_tx_assets_transfer_true {
//     (state == 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     exists f2: method .
//     exists args2: calldataargs .
//     exists msgvalue2 : int .
//     (<< addr : Vault . f1(args1) $ msgvalue1 >>		
//         block.number >= request_time + wait_time
//         -> 
//         << addr : Vault . f2(args2) $ msgvalue2 >>		
//               (balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
//               //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }


// rule Tx_tx_assets_transfer_false {
//     (state == 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     exists f2: method .
//     exists args2: calldataargs .
//     exists msgvalue2 : int .
//     (<< addr : Vault . f1(args1) $ msgvalue1 >>		
//         << addr : Vault . f2(args2) $ msgvalue2 >>		
//               (balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)) + 1)
//               //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }

// rule Tx_tx_assets_transfer_no_attack {
//     (state == 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     exists f2: method .
//     exists args2: calldataargs .
//     exists msgvalue2 : int .
//     forall adversary: address .
//     (
//       (
//       forall f_adversary: method .
//       forall args_adversary: calldataargs .
//       forall msgvalue_adversary : int .
//       (adversary != addr && adversary != recovery)
//       ->
//       ((<< addr : Vault . f1(args1) $ msgvalue1 >>		
//         << adversary : Vault . f_adversary(args_adversary) $ msgvalue_adversary >>		
//           << addr : Vault . f2(args2) $ msgvalue2 >>		
//                 (balance[recipient] == old(old(old(balance[recipient]))) + amount)
//                // (balance[recipient] == old(old(balance[recipient])) + amount)
//                )
//       ))
//     ))
// }



// rule Tx_tx_assets_transfer_no_attack_False {
//     (state == 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     exists f2: method .
//     exists args2: calldataargs .
//     exists msgvalue2 : int .
//     forall adversary: address .
//     ((adversary != addr && adversary != recipient)
//     ->
//       (
//       forall f_adversary: method .
//       forall args_adversary: calldataargs .
//       forall msgvalue_adversary : int .
//       (<< addr : Vault . f1(args1) $ msgvalue1 >>		
//         << adversary : Vault . f_adversary(args_adversary) $ msgvalue_adversary >>		
//           << addr : Vault . f2(args2) $ msgvalue2 >>		
//                 (balance[recipient] == old(old(old(balance[recipient]))) + old(amount) +1)
//                // (balance[recipient] == old(old(balance[recipient])) + amount + 1)
//       ))
//     ))
// }

// rule Fin_owner_liquid_true {
//     (state == 1 && block.number >= request_time + wait_time
//     ) ->
//     (exists f: method .
//     exists args: calldataargs .
//     exists msgvalue : int .
//     (<< owner : Vault . f(args) $ msgvalue >>		
//               (balance[receiver]>= old(balance[receiver]) + amount)
//     ))
// }



/*
// liquid after the deadline has passed
property fin_owner_liquid {
    Forall xa
      [
        state==1 && block.number >= request_time + wait_time
          -> 
        Exists tx [1, owner]
        [
          ((<tx>balance[receiver] >= balance[receiver] + amount))
        ]
      ]
}

property canc_recovery_liquid {
    Forall xa
      [
        state==1 && block.number < request_time + wait_time
          -> 
        Exists tx [1, recovery]
        [
          (<tx>state == 0)
        ]
      ]
}

// notliquid because all the transactions in tx must be in the same block
property wd_fin_owner_notliquid {
    Forall xa
      [
        state==0 
          -> 
        Exists tx [2, owner]
        [
          ((<tx>balance[xa] >= balance[xa] + balance))
        ]
      ]
}
*/