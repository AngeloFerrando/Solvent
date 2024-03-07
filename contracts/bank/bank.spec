property liq1 {
    Forall xa
      [
        st.balances[xa]>0 
          -> 
        Exists tx [1, xa]
        [
          (app_tx_st.balance[xa] - st.balance[xa] >= st.balances[xa])
        ]
      ]
}