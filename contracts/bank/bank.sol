contract Bank {
    (address -> int) myBalances

    constructor() {
        skip
    }

    function deposit() payable {
        myBalances[msg.sender] = myBalances[msg.sender] + msg.value
    }

    function withdraw(int amount) {
        require(amount > 0);
        require(amount <= myBalances[msg.sender]);

        myBalances[msg.sender] = myBalances[msg.sender] - amount;
        msg.sender!amount
    }
}  

// ? WEAK UNSAT ?
property live1 {
    Forall xa
      [
        st.myBalances[xa]>0 
          -> 
        Exists tx [1, xa]
        [
          (app_tx_st.balance[xa] - st.balance[xa] >= st.myBalances[xa])
        ]
      ]
}