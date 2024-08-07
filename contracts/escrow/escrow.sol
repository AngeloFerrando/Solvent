// Adapted from: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/escrow

// States: 
// 0 = AGREE
// 1 = DISPUTE 
// 2 = ARBITRATED 
// 3 = REDEEM
// 4 = END

contract Escrow {
  int state;
  address buyer;
  address seller;
  address arbiter;
  int fee;
  int deposit;       // buyer's deposit
  address recipient; // recipient agreed or chosen by the arbiter
 
  constructor(address seller_, address arbiter_, int fee_) payable {
    require(seller_ != 0 && arbiter_ != 0);
    require(fee_>=0 && fee_ < msg.value);    // The fee cannot be more than the deposit
    buyer = msg.sender;
    seller = seller_;
    arbiter = arbiter_;
    fee = fee_;
    state = 0
  }
 
  function approve_payment() {
    require(state==0); // AGREE
    require(msg.sender == buyer); 
    state = 3; // REDEEM
    recipient = seller      
  }

  function refund() {
    require(state==0); // AGREE
    require(msg.sender == seller);
    state = 3; // REDEEM
    recipient = buyer
  }

  function open_dispute() {
    require(state==0); // AGREE
    require(msg.sender == buyer || msg.sender == seller);
    state = 1 // DISPUTE
  }

  function arbitrate(address dst) {
    require(state==1); // DISPUTE
    require(msg.sender == arbiter);
    require(dst == buyer || dst == seller);
    recipient = dst;
    state = 3; // REDEEM
    deposit = deposit - fee;
    arbiter.transfer(fee)
  }

  function redeem() {
    require(state==3); // REDEEM
    state = 4; // END
    recipient.transfer(deposit)
  }
}

// if a dispute is open, then the arbiter can redeem the fee
property arbiter_wd_fee_liquid {
    Forall xa
      [
        state==1 
          -> 
        Exists tx [1, arbiter]
        [
          <tx>balance[arbiter] == balance[arbiter] + fee
        ]
      ]
}

// if the arbiter has resolved the dispute, then either the buyer or the seller can redeem the deposit
property buyerorseller_wd_deposit_liquid {
    Forall xa
      [
        state==3 && (xa==buyer || xa==seller) 
          -> 
        Exists tx [1, xa]
        [
          <tx>balance[xa] >= balance[xa] + deposit
        ]
      ]
}

// if the arbiter has resolved the dispute, then anyone can redeem the whole contract balance
property anyone_wd_notliquid {
    Forall xa
      [
        state==3 
          -> 
        Exists tx [1, xa]
        [
          <tx>balance[xa] >= balance[xa] + balance
        ]
      ]
}

// in the Agree state, both the buyer and the seller can open a dispute
property dispute_if_agree_liquid {
    Forall xa
      [
        state==0 && (xa==buyer || xa==seller) 
          -> 
        Exists tx [1, xa]
        [
          <tx>state==1
        ]
      ]
}
// dispute_if_agree is expressible and verifiable in Certora: https://github.com/fsainas/contracts-verification-benchmark/tree/main/contracts/escrow

// once one of the participants has redeemed the deposit, anyone can withdraw the whole contract balance 
property no_frozen_funds_notliquid {
    Forall xa
      [
        state==4 && balance>0 
          -> 
        Exists tx [1, xa]
        [
          <tx>balance[xa] == balance[xa] + balance
        ]
      ]
}