// certoraRun transfer.sol:Transfer --verify Transfer:transfer.spec

methods {
    function withdraw(uint) external;
    function getBal(address) external returns(uint) envfree; 
}

rule wd {
    env e;
    uint v;
    
    mathint oldb = getBal(currentContract.rcv);

    withdraw(e, v);
    
    mathint newb = getBal(currentContract.rcv);

    assert(newb == oldb + to_mathint(v));
}
