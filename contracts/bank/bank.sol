contract Bank {
    mapping (address => int) balances

    function deposit() payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(amount) {
        require(amount > 0);
        require(amount <= balances[msg.sender]);

        balances[msg.sender] -= amount;

        msg.sender!amount
    }
}  

property liq1 {
    Forall xa
      [
        st.Bank.balances[xa]>0 
          -> 
        Exists tx [1, xa]
        [
          (app_tx_st.xa.balance() - st.xa.balance() >= st.Bank.balances[xa])
        ]
      ]
}