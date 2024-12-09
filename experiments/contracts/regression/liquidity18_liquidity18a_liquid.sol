contract C18 {

  int count;

  constructor() {
    skip
  }

  function pay(int amount) {
    require (amount <= balance); // se è falso, lo stato nuovo della blockchain è uguale a quello vecchio
    sender.transfer(1);
    require (amount - 1 <= balance);
    sender.transfer(amount - 1)
    // se sono arrivato qui, allora lo stato nuovo della blockchain è uguale all'ultimo stato della computazione interna
  }

}

// STRONG UNSAT
// liquid
property  liquidity18a_liquid {
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