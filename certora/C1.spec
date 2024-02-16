// certoraRun C1.sol --verify Liq1:Liquidity.spec

methods {
    function pay() external;    
    function getBal(address) external returns (uint) envfree;
}

// Liq1 checks that every call to withdraw does not revert.
// This implicitly implies that the low-level call in C1 succeds,
// and so the the whole contract balance is transferred to msg.sender
// Note that msg.sender could be a contract, which in turns transfers
// again the funds.

rule Liq1(address sender) {
    // mathint b0 = getBal(sender);
    env e;
    
    require(e.msg.value == 0);
    pay@withrevert(e);

    // mathint c0 = getBal(currentContract);
    // assert(c0 == 0);

    assert(!lastReverted);
}
