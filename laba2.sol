// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract RockPaperScissors {
    address payable public player1;
    address payable public player2;
    uint public bet = 200000000000000; // 0.0002 ETH in wei
    uint public player1Choice;
    uint public player2Choice;
    bool public gameFinished;

    function makeChoice(uint choice) public {
        require(msg.sender == player1 || msg.sender == player2, "You are not a player in this game.");
        require(player1Choice == 0 || player2Choice == 0, "You have already made your choice.");
        require(choice >= 1 && choice <= 3, "Invalid choice. Choose 1 for rock, 2 for paper, or 3 for scissors.");
        if (msg.sender == player1 && player1Choice == 0) {
            player1Choice = choice;
        } else {
            player2Choice = choice;
        }
    }

    function getWinner() public {
        require(player1Choice != 0 && player2Choice != 0, "Both players must make their choice before getting the result.");
        require(!gameFinished, "The game has already finished.");
        gameFinished = true;
        if (player1Choice == player2Choice) {
            resetGame();
        } else if ((player1Choice == 1 && player2Choice == 3) || (player1Choice == 2 && player2Choice == 1) || (player1Choice == 3 && player2Choice == 2)) {
            player1.transfer(bet);
            resetGame();
        } else {
            player2.transfer(bet);
            resetGame();
        }
    }

    function joinGame() public payable {
        require(player1 == address(0) || player2 == address(0), "This game is already full.");
        
        if (player1 == address(0)) {
            player1 = payable(msg.sender);
            if (player1.balance < bet) {
                resetGame();
            } 
        } else {
            player2 = payable(msg.sender);
            if (player2.balance < bet) {
                resetGame();
            }
        }
    }

    function resetGame() private {
        player1Choice = 0;
        player2Choice = 0;
        gameFinished = false;
        player1 = payable(address(0));
        player2 = payable(address(0));
    }
}

