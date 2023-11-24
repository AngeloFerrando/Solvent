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