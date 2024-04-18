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
        msg.sender!amount
    }
}  

property  deposit_not_revert_live {
    Forall xa
      [
        st.balance[xa]>0 
          -> 
        Exists tx [1, xa]
        [
          (app_tx_st.funds[xa] == st.funds[xa] + st.balance[xa])
        ]
      ]
}


