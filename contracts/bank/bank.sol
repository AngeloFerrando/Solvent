contract Bank {
    (address -> int) myBalances

    function deposit() payable {
        myBalances[msg.sender] = myBalances[msg.sender] + msg.value
    }

    function withdraw(amount) {
        require(amount > 0);
        require(amount <= myBalances[msg.sender]);

        myBalances[msg.sender] = myBalances[msg.sender] - amount;
        msg.sender!amount
    }
}  

property liq1 {
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