
contract StateChange1 {
    
    address owner
    int state

    constructor(o) {
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

property live_nonliq {
    Forall xa
    [
      state==0
        ->
      Exists tx [1, st.owner]
      [
        state==1
      ]
    ]
}

property not_live_nonliq {
    Forall xa
    [
      state==2
        ->
      Exists tx [1, st.owner]
      [
        state==1
      ]
    ]
}
