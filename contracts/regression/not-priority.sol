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
// so the property is trivially true since the antecedent of the implication is false 
property p1_notlive {
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

// the property should be false, because the contract could not have enough balance to pay 
property p2_notlive {
    Forall xa
    [
      (!false) || true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa] + 1000))
      ]
    ]
}

// the property should be false, because the contract could not have enough balance to pay 
property p3_live {
    Forall xa
    [
      !true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa] + 1000))
      ]
    ]
}
