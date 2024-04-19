contract Lottery {
    address player1
    address player2

    const int end_commit		// last round to join
    const int end_reveal		// last round to reveal

    hash hashlock1
    hash hashlock2

    secret secret1
    secret secret2

    int state

    constructor(int tc, int tr) {
        require (tc < tr);
        end_commit = tc;
        end_reveal = tr;
        state = 0 // next = join1
    }

    function join1(address a1, hash h1) payable {
        require (state == 0);
        require (msg.value == 1);
        player1 = a1;
        hashlock1 = h1;
        state = 1 // next = join2 or redeem1_nojoin
    }

    function join2(address a2, hash h2) payable {
        require (state == 1);
        require (h2 != hashlock1);
        require (msg.value == 1);
        player2 = a2;
        hashlock2 = h2;
        state = 2 // next = reveal1
    }

    // if, after the commit deadline, the second player has not joined,
    // then player1 can redeem the bet 
    function redeem1_nojoin() {
        require (state == 1);
        require (block.number >= end_commit);
        player1!balance;
        state = 3 // next = end
    }

    // player1 must reveal first
    function reveal1(secret s1) {
        require (state == 2);
        require (block.number >= end_commit);
        require (sha256(s1) == hashlock1);
        secret1 = s1;
        state = 4 // next = reveal2 or redeem2_noreveal
    }

    // player2 must reveal after player1
    // the deadline extension +100 is needed to avoid attacks where 
    // player1 reveals close to the deadline, 

    function reveal2(secret s2) {
        require (state == 4);
        require (block.number >= end_reveal + 100);
        require (sha256(s2) == hashlock2);
        secret2 = s2;
        state = 5 // next = win
    }

    // if player1 has not revealed, player2 can redeem the pot
    function redeem2_noreveal() {
        require (state == 2);
        require (block.number >= end_reveal);
        player2!balance;
        state = 3 // next = end
    }

    function redeem1_noreveal() {
        require (state == 4);
        require (block.number >= end_reveal+100);
        player1!balance;
        state = 3 // next = end
    }

    function win() {
        require (state == 5);

        if ((length(secret1) + length(secret2)) % 2 == 0) {
            player1!balance
        }
        else {
            player2!balance
        };

        state = 3 // next = end
    }
}

property  player1_can_redeem_nojoin_live {
    Forall xa
    [
      st.state == 1 && st.block.number >= st.end_commit
        ->
      Exists tx [1, xa]
      [
        (app_tx_st.balance[player1] == st.balance[player1]  + st.balance )  
      ]
    ]
} 

