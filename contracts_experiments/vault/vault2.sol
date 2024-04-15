// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/vault

contract Vault {
    address owner
    address recovery
    int wait_time

    address receiver
    int request_time
    int amount
    int state
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
        receiver!amount
    }

    function cancel() {
        require(state == 1); // REQ
        require(msg.sender == recovery);
        state = 0 // IDLE
    }
}

property canc_recovery_live {
    Forall xa
      [
        st.state==1 && st.block.number < st.request_time + st.wait_time
          -> 
        Exists tx [1, st.recovery]
        [
          (app_tx_st.state == 0)
        ]
      ]
}
