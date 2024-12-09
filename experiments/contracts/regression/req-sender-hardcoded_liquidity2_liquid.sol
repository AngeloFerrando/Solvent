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

property  liquidity2_liquid {
    Forall xa
    [
      xa == 1
        ->
      Exists tx [1, xa]
      [
        ((<tx>balance[xa] == balance[xa]  + balance))
      ]
    ]
}