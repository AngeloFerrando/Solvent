contract C14 {
  bool b

  constructor () {
    b = False;
    skip
  }

  function unlock() {
    require(not b); 
    b = true
  }

  function pay(int amount) {
    require (amount <= balance && b);
    b = False;
    sender ! amount
  }

}

/*
// not liquid
property liquidity14a_nonlive {
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


// liquid
property liquidity14b_live {
    Forall xa
    [
      st.b == true
        ->
      Exists tx [1, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance))
      ]
    ]
}
*/


//  liquid
property liquidity14c_live {
    Forall xa
    [
      true
        ->
      Exists tx [2, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance ))
      ]
    ]
}

//  liquid
property liquidity14d_live {
    Forall xa
    [
      st.b==true
        ->
      Exists tx [2, xa]
      [
        ((app_tx_st.balance[xa] == st.balance[xa]  + st.balance ))
      ]
    ]
}
