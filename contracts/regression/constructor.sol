contract Constructor1 {

  constructor() payable {
    require(msg.value==0)
  }

  function pay(int amount) {
    msg.sender.transfer(1)
  }
}

rule Paynotrevert {
  forall a : address .
  exists v : int . 
    <a : Constructor1 . pay(v) $ 0> !lastReverted
}



