
contract StateChange1 {
    
    address owner
    int state

    constructor(address o) {
        owner = o;
        state = 0
    }

    function foo() {
        // require(msg.sender == owner);
        require(state == 0);
        state = 1
    }

    function fie() {
        // require(msg.sender == owner);
        require(state == 0);
        state = 2
    }

}

property  liquid_nonliquid {
    Forall xa
    [
      state==0
        ->
      Exists tx [1, owner]
      [
        state==1
      ]
    ]
}

