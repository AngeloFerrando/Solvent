// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/vault

contract Vault {
    address owner;
    address recovery;
    uint wait_time;

    address receiver;
    int request_time;
    int amount;
    int state;
    // 0 = IDLE
    // 1 = REQ
   
    constructor (address recovery_, int wait_time_) payable {
    	require(msg.sender != recovery_);
      require(wait_time_ >= 0);
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

rule Dummy_true {
    (state == 0 && balance == 0) ->
    (
    exists recipient: address .
    true
    )
}

rule Dummy_false {
    (state == 0 && balance == 0) ->
    (
    exists recipient: address .
    state ==1
    )
}


rule Tx_tx_assets_transfer_trace_false2 {
    (state == 0 && balance == 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
        //block.number >= request_time + wait_time
        //true
        //->
        << owner : Vault . finalize() $ 0 >>		
              //(balance[recipient] ==  old(old(balance[recipient]))  )
              //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
              (balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
    ))
}

rule Tx_tx_assets_transfer_trace_true {
    (state == 0 && balance > 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
        //block.number >= request_time + wait_time
        //true
        //->
        << owner : Vault . finalize() $ 0 >>		
              (balance[recipient] ==  old(old(balance[recipient]))  )
              //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
              //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
    ))
}

// valid (k=1)
rule Withdraw_State_change_true {
    (state == 0 && balance > 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>	
      !lastReverted
      &&
      receiver == recipient
      &&
      amount == old(balance)
    ))
}

// invalid after 0 steps
rule Withdraw_State_change_false {
    (state == 0 && balance > 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>	
      !lastReverted
      &&
      receiver == recipient
      &&
      amount == old(balance)+1
    ))
}

/////// true up to 8 steps
// false if receiver is address 0 !
rule Finilize_assets_transfer_false_address0 {
    (state == 1 && balance > 0 && amount > 0 && block.number >= request_time + wait_time) ->
        << owner : Vault . finalize() $ 0 >>		
              (balance[receiver] ==  old(balance[receiver]) +  amount  )
}

//invalid after 1 steps
rule Finilize_assets_transfer_false {
    (state == 1 && balance > 0 && amount > 0 && block.number >= request_time + wait_time) ->
        << owner : Vault . finalize() $ 0 >>		
              (balance[receiver] ==  old(balance[receiver]) +  amount + 1 )
}

//  valid (k=1)
rule Tx_tx_assets_transfer_trace_balance_true {
    (state == 0 && balance > 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
        //block.number >= request_time + wait_time
        //true
        //->
        << owner : Vault . finalize() $ 0 >>		
              (balance[recipient] ==  old(old(balance[recipient])) +  old(old(balance))  )
    ))
}

//invalid after 0 steps
rule Bal_leq0_false {
  balance <= 0
}

//invalid after 0 steps
rule Bal_leq0_or_State0_false {
  not(state == 0 && balance > 0) 
}

//  invalid after 0 steps
rule Tx_tx_assets_transfer_trace_balance_false {
    (state == 0 && balance > 0) ->
    (
    exists recipient: address .
    (<< owner : Vault . withdraw(recipient, balance) $ 0 >>		
        //block.number >= request_time + wait_time
        //true
        //->
        << owner : Vault . finalize() $ 0 >>		
              (balance[recipient] ==  old(old(balance[recipient])) +  old(old(balance)) + 1000 )
              //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
              //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
    ))
}

rule Tx_tx_assets_transfer_nostate0_false {
    (exists addr: address .
    exists recipient: address .
    exists f1: method .
    exists args1: calldataargs .
    exists msgvalue1 : int .
    exists f2: method .
    exists args2: calldataargs .
    exists msgvalue2 : int .
    (<< addr : Vault . f1(args1) $ msgvalue1 >>		
        << addr : Vault . f2(args2) $ msgvalue2 >>		
              (balance[recipient] ==  old(old(balance[recipient] +balance)))
    ))
}

// valid (k=1)
rule Tx_tx_assets_transfer_true {
    (state == 0) ->
    (exists addr: address .
    exists recipient: address .
    exists f1: method .
    exists args1: calldataargs .
    exists msgvalue1 : int .
    exists f2: method .
    exists args2: calldataargs .
    exists msgvalue2 : int .
    (<< addr : Vault . f1(args1) $ msgvalue1 >>		
        << addr : Vault . f2(args2) $ msgvalue2 >>		
              (balance[recipient] ==  old(old(balance[recipient] +balance)))
    ))
}


rule Tx_tx_assets_transfer_noBlockNum_interleaving_true {
    (state == 0 && balance > 0) ->
    (exists addr: address .
    exists recipient: address .
    exists f1: method .
    exists args1: calldataargs .
    exists msgvalue1 : int .
    exists f2: method .
    exists args2: calldataargs .
    exists msgvalue2 : int .
    (<< addr : Vault . f1(args1) $ msgvalue1 >>		
         block.number == old(block.number)
         &&
        << addr : Vault . f2(args2) $ msgvalue2 >>		
              (balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
    ))
}

// valid (k=1)
rule IsPossible_noBlockNum_interleaving_true {
    (state == 0 && balance > 0) ->
    (exists addr: address .
    exists recipient: address .
    exists f1: method .
    exists args1: calldataargs .
    exists msgvalue1 : int .
    exists f2: method .
    exists args2: calldataargs .
    exists msgvalue2 : int .
    (<< addr : Vault . f1(args1) $ msgvalue1 >>		
         block.number == old(block.number)
    ))
}

// <Error> Parser error at outputTrace.lus:596:29: Unknown identifier 'constructor_recovery__args2_tx'
// rule Tx_tx_assets_transfer_blocknumber_false_parserror {
//     (state == 0 && balance > 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     (<< addr : Vault . f1(args1) $ msgvalue1 >>		
//         block.number <= old(block.number)+2
//         -> 
//         (exists f2: method .
//         exists args2: calldataargs .
//         exists msgvalue2 : int .
//         << addr : Vault . f2(args2) $ msgvalue2 >>		
//               (balance[recipient] ==  old(old(balance[recipient])) + old(old(balance))))
//               //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }

// this is not really expressible (at least for now), since we would need to re-quantify (universally) the blocknumber, but now it is implicitly quantified existentially
// rule Tx_tx_assets_transfer_blocknumber_false {
//     (state == 0 && balance > 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     exists f2: method .
//     exists args2: calldataargs .
//     exists msgvalue2 : int .
//     (<< addr : Vault . f1(args1) $ msgvalue1 >>		
//         block.number <= old(block.number)+2
//         -> 
//         (
//         << addr : Vault . f2(args2) $ msgvalue2 >>		
//               (balance[recipient] ==  old(old(balance[recipient])) + old(old(balance))))
//               //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
//     ))
// }



// invalid after 0 steps
rule Tx_tx_assets_transfer_plus1000_false {
    (state == 0 && balance > 0) ->
    (exists addr: address .
    exists recipient: address .
    exists f1: method .
    exists args1: calldataargs .
    exists msgvalue1 : int .
    exists f2: method .
    exists args2: calldataargs .
    exists msgvalue2 : int .
    (<< addr : Vault . f1(args1) $ msgvalue1 >>		
        // block.number >= request_time + wait_time
        // -> 
        << addr : Vault . f2(args2) $ msgvalue2 >>		
              //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
              //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
              (balance[recipient] == old(old(balance[recipient])) + old(old(balance)) + 1000)
    ))
}

// bug <Error> Parser error at out/outputTrace.lus:284:34: Unknown identifier 'aw_1_nx10'
// rule Tx_tx_assets_transfer_no_interleaving_attack_true {
//     (state == 0 && balance > 0) ->
//     (exists addr: address .
//     exists recipient: address .
//     exists f1: method .
//     exists args1: calldataargs .
//     exists msgvalue1 : int .
//     exists f2: method .
//     exists args2: calldataargs .
//     exists msgvalue2 : int .
//     //forall adversary: address .
//     // (adversary != addr && adversary != recovery)
//     // ->
//     (
//     << addr : Vault . f1(args1) $ msgvalue1 >>		
//       // forall f_adversary: method .
//       // forall args_adversary: calldataargs .
//       // forall msgvalue_adversary : int .
//         //<< adversary : Vault . f_adversary(args_adversary) $ msgvalue_adversary >>		
//         (
//           // block.number == old(block.number)
//           // &&
//         << addr : Vault . f2(args2) $ msgvalue2 >>		
//               (balance[recipient] ==  old(old(old(balance[recipient]))) + old(old(old(balance))))
//               //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)) + 1000)
//         )
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

// false if receiver is address 0 !
rule Fin_owner_liquid_false {
    (state == 1 && block.number >= request_time + wait_time
    ) ->
    (exists f: method .
    exists args: calldataargs .
    exists msgvalue : int .
    (<< owner : Vault . f(args) $ msgvalue >>		
              (balance[receiver]>= old(balance[receiver]) + amount)
    ))
}


