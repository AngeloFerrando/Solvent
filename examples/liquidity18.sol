contract C18 {

  int count

  constructor() {
    skip
  }

  function pay(amount) {
    require (amount <= balance); // se è falso, lo stato nuovo della blockchain è uguale a quello vecchio
    sender ! 1;
    require (amount - 1 <= balance);
    sender ! amount - 1
    // se sono arrivato qui, allora lo stato nuovo della blockchain è uguale all'ultimo stato della computazione interna
  }

}

// liquid
property liquidity18a_liq {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}