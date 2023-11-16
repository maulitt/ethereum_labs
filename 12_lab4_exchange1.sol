// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// мои токены:
import "./10_lab4_tokenA.sol";
import "./11_lab4_tokenB.sol";

contract TokenExchange {
    TokenA public tokenA;
    TokenB public tokenB;

    event TokensExchanged(address indexed from, address indexed to, uint256 amount, string fromToken, string toToken);

    constructor(address _tokenA, address _tokenB) {
        tokenA = TokenA(_tokenA);
        tokenB = TokenB(_tokenB);
    }

    function getTokensA(uint256 amount) external {
        tokenA.transfer(msg.sender, amount);
    }

    function getTokensB(uint256 amount) external {
        tokenB.transfer(msg.sender, amount);
    }

    function exchangeAToB(uint256 amount) external {
        require(tokenA.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        uint256 amountB = amount / 2; // курс - 1 токенБ = 0.5 токенА
        tokenB.transfer(msg.sender, amountB);
        emit TokensExchanged(msg.sender, address(this), amount, "TokenA", "TokenB");
    }

    function exchangeBToA(uint256 amount) external {
        require(tokenB.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        uint256 amountA = amount * 2; // курс - 1 токенБ = 0.5 токенА
        tokenA.transfer(msg.sender, amountA);
        emit TokensExchanged(msg.sender, address(this), amount, "TokenB", "TokenA");
    }
}