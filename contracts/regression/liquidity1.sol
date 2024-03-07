contract C1 {
  int maxCount
  int count	// implicitamente inizializzato a 0
  address owner // anche questo implicitamente inizializzato a 0, ma impostato dal costruttore

  constructor() {
    owner = msg.sender;
    maxCount = 1;
    count = 0
  } 
  
  function pay() {
    require (count<maxCount);
    if (msg.sender==owner) { 
        count=count+1 
    }
    else { 
        count = count;
        msg.sender!balance 
    }
  }
}
