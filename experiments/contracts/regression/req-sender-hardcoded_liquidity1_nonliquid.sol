/// @custom:version liquidity3

contract C {

  constructor () {
    skip
  }

  function pay(int amount) {
    require (amount<=balance && msg.sender==1);
    msg.sender.transfer(amount)
  }
}

property  liquidity1_nonliquid {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa]  + balance))
      ]
    ]
}

