// certoraRun freezable.sol:Freezable --verify Freezable:freezable.spec

methods {
    function freeze() external;    
    function withdraw(uint) external;
    function getBal(address) external returns (uint) envfree;
}

rule wd_satisfy(address sender, uint amount) {
    mathint b0 = getBal(sender);
    env e;
    
    require e.msg.sender == sender;
    withdraw(e, amount);
 
    mathint b1 = getBal(sender);
    satisfy(b1 == b0+amount);
}

rule wd_assert(address sender, uint amount) {
    mathint b0 = getBal(sender);
    env e;
    
    require e.msg.sender == sender;
    withdraw(e, amount);
 
    mathint b1 = getBal(sender);
    assert(b1 == b0+amount);
}
