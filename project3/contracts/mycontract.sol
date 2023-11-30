// SPDX-License-Identifier: UNLICENSED

// DO NOT MODIFY BELOW THIS
pragma solidity ^0.8.17;

import "hardhat/console.sol";

contract Splitwise {
    // DO NOT MODIFY ABOVE THIS

    // ADD YOUR CONTRACT CODE BELOW

    // data structure used to save the debts
    mapping(address => mapping(address => uint32)) private debts;

    // function to add two uint32 numbers and check for overflow
    function add(uint32 a, uint32 b) private pure returns (uint32) {
      uint32 c = a + b;
      require(c >= a);
      return c;
    }

    // function takes a potential debt cycle and the value it can be reduced by, 
    // checks if the cycle is valid and removes the debt if it is
    function check_cycle(address[] memory cycle, uint32 cycle_val) private returns (bool ret) {
        if (cycle[0] != cycle[cycle.length - 1]) {
            return false;
        }

        if (cycle.length > 10) {
            return false;
        }

        for (uint i = 1; i < cycle.length; i++) {
            if (debts[cycle[i-1]][cycle[i]] < cycle_val) {
                return false;
            }
        }

        for (uint i = 1; i < cycle.length; i++) {
            debts[cycle[i-1]][cycle[i]] -= cycle_val;
        }

        return true;
    }

    // function to check how much a debtor owes to a creditor
    function lookup(address debtor, address creditor) public view returns (uint32) {
        return debts[debtor][creditor];
    }

    // function to add a new debt
    function add_IOU(address creditor, uint32 amount, address[] memory cycle, uint32 cycle_val) public {
        require(amount > 0, "Amount has to be positive!");
        require(creditor != msg.sender, "Debtor equal to creditor!");

        debts[msg.sender][creditor] += add(debts[msg.sender][creditor], amount);

        if (cycle_val != 0){
            require(check_cycle(cycle, cycle_val), "Invalid cycle was specified!");
        }
    }
}
