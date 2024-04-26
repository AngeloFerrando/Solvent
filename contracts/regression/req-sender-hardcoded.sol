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

property liquidity1_nonlive {
    Forall xa
    [
      true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == balance[xa]  + balance))
      ]
    ]
}

property liquidity2_live {
    Forall xa
    [
      xa == 1
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == balance[xa]  + balance))
      ]
    ]
}