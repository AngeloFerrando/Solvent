
// regression from Vault.sol

contract Vault {
    address owner;
    int state;
    // 0 = IDLE
    // 1 = REQ
   
    constructor ()  {
        owner = msg.sender;
        state = 0 // IDLE
    }

    function withdraw() {
        state = 1 // REQ
    }

    function finalize() {
        require(state == 1); // REQ
        state = 0 // IDLE	
    }

}

rule Dummy_true {
    (
      << owner : Vault . withdraw() $ 0 >>		
        << owner : Vault . finalize() $ 0 >>	
          true	
              //(balance[recipient] ==  old(old(balance[recipient]))  )
              //(balance[recipient] ==  old(old(balance[recipient])) + old(old(balance)))
              //(balance[recipient] == old(old(balance[recipient])) + old(amount) + 1000)
    )
}
