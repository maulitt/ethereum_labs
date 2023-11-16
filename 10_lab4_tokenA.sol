// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// import "./IERC20.sol";

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TokenA is ERC20 {
    event TokensSent(address indexed from, address indexed to, uint256 amount);

    constructor() ERC20("TokenA", "TKA") {
        _mint(msg.sender, 1000000 * (10 ** uint256(decimals())));
    }

    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        emit TokensSent(msg.sender, recipient, amount);
        return super.transfer(recipient, amount);
    }
}