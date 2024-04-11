contract NotPriority {
    bool b

    constructor() {
      skip
    }

    function pay() {
      msg.sender!1
    }
}

// not should have priority over ||. 
// Here not false || true seems to be paranthesized as not (false || true) = false, 
// so the property is trivially true since the antecedent of the implication is false 
property p1_live {
    Forall xa
    [
      not false || true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa] + 1000))
      ]
    ]
}

// the property should be false, because the contract could not have enough balance to pay 
property p2_live {
    Forall xa
    [
      (not false) || true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa] + 1000))
      ]
    ]
}
