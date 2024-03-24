contract Crowdfund {
    int deadline                        // deadline for donations
    int target                          // the campaign is successful is this target is reaches 
    address owner                       // beneficiary of the campaign
    int min_donation                    // minimum donation
    (address -> int) funds             // keeps track of the donations

    constructor(d t o m) {
        owner = o;
        deadline = d; 
        target = t;
        min_donation = m
    }

    function deposit(a) payable {
        require (block.number <= deadline);
        require (msg.value>=min_donation);
       	funds[msg.sender] = funds[msg.sender] + msg.value
    } // next(deposit,finalize)

    function finalize() {
        require (block.number > deadline); // questo sembra rompere la liquidity
       	if (balance >= target) {
         	owner!balance
        }
    }

// vorrei poterla scrivere come segue, ma da' errore
/*
    function withdraw() {
       	msg.sender!myfunds[msg.sender];
       	myfunds[msg.sender] = 0
    }
*/

    function withdraw(amount) {
        require (amount <= funds[msg.sender]); // workaround per risolvere problema di sintassi
        require (balance < target);
        require (block.number > deadline);
       	msg.sender!amount;
       	funds[msg.sender] = 0
    }
}

// should be true: seller can withdraw the balance after the deadline
property ownerCanWithdraw_liq {
    Forall xa
    [
      st.balance >= st.target
        ->
      Exists tx [1, st.owner]
      [
        ((app_tx_st.balance[st.owner] >= st.balance[st.owner] + st.target))
      ]
    ]
}