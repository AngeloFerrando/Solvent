contract Mapping1 {
    mapping (address => int) m

    function foo() {
        m[msg.sender] = m[msg.sender] + 1
    }
}  

property live1 {
    Forall xa
      [
        true 
          -> 
        Exists tx [1, xa]
        [
          (app_tx_st.m[xa] == st.m[xa] + 1)
        ]
      ]
}
