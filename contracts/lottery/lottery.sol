contract Lottery {
    address player1
    address player2

    int end_commit		// last round to join
    int end_reveal		// last round to reveal

    hash hashlock1
    hash hashlock2

    secret secret1
    secret secret2

     
    constructor(int tc, int tr) {
        require (tc < tr);
        end_commit = tc;
        end_reveal = tr;
        state = 0 // next = join1
    }

    function join1(address a, hash h) payable {
        require (state == 0);
        require (msg.value == 1);
        player1 = a;
        hashlock1 = h;
        state = 1 // next = join2 or redeem1_nojoin
    }

    function join2(address a, hash h) payable {
        require (state == 1);
        require (h != hashlock1);
        require (msg.value == 1);
        player2 = a;
        commitment2 = h;
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
    function reveal1(secret s) {
        require (state == 2);
        require (block.number >= end_commit);
        require (sha256(s) == hashlock1);
        secret1 = s;
        state = 4 // next = reveal2 or redeem2_noreveal
    }

    // player2 must reveal after player1
    // the deadline extension +100 is needed to avoid attacks where 
    // player1 reveals close to the deadline, 

    function reveal2(secret s) {
        require (state == 4);
        require (block.number >= end_reveal + 100);
        require (sha256(s) == commitment2);
        secret2 = s;
        state = 5 // next = win
    } next(win)

    // if player1 has not revealed, player2 can redeem the pot
    function redeem2_noreveal() {
        require (state == 4);
        require (block.number >= end_reveal);
        player2!balance;
        state = 3 // next = end
    }

    function redeem1_noreveal() {
        require (state == 2);
        require (block.number >= end_reveal+100)
        player1!balance;
        state = 3 // next = end
    }

    function win() {
        require (state == 5);

        if ((length(secret1) + length(secret2)) % 2 == 0)
            player1!balance
        else
            player2!balance

        state = 3 // next = end
    }
}