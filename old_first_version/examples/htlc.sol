contract HTLC {
   address payable public owner;  
   address payable public verifier;
   bytes32 public hash;
   uint start;
 
   constructor(address payable v) {
       owner = payable(msg.sender);
       verifier = v;
       start = block.number;
   }
 
   function commit(bytes32 h) public payable {
       require (msg.sender==owner);
       require (msg.value >= 1 ether);
       hash = h;
   }
 
   function reveal(string memory s) public {
       require (msg.sender==owner);
       require(keccak256(abi.encodePacked(s))==hash);
       owner.transfer(address(this).balance);
   }
 
   function timeout() public {
       require (block.number > start + 1000);
       verifier.transfer(address(this).balance);
   }
}
