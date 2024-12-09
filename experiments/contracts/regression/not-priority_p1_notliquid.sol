contract NotPriority {
    bool b;

    constructor() {
      skip
    }

    function pay() {
      msg.sender.transfer(1)
    }
}

// not should have priority over ||. 
// Here not false || true seems to be parenthesized as not (false || true) = false, 
// so the it is trivially true since the antecedent of the implication is false 
property  p1_notliquid {
    Forall xa
    [
      !false || true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa] + 1000))
      ]
    ]
}

// it should be false, because the contract could not have enough balance to pay 
