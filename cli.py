# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


# from logic import Logic
# from tests import Test

import numpy as np


class Cli:

    def __init__(self):
        self.board = []
        self.logic = Logic()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
    
    def computer_move(self, computer):
        empty = np.argwhere(np.array(self.board) == "-")
        spot = np.random.randint(empty.shape[0])
        row, col = empty[spot]
        self.board[row][col] = computer
    
    def start(self):
        self.create_board()
        
        print("Choose mode")
        mode = input("Type 1 Player or 2 Players: ")
        print(mode)

        player = 'X' if self.logic.get_random_first_player() == 1 else 'O'
        print()
        
        if mode == "1 Player":
            print("player is " + player)
            computer = 'O' if player == 'X' else 'X'
            print("computer is " + computer)
            print()
            
            computer_first = self.logic.get_random_first_player()
            
            if computer_first == 1:
                print("Computer moves first")
            else:
                print("Player moves first")
            
            print()


        if mode == "2 Players":
            while True:
                print(f"Player {player} turn")

                self.show_board()
        
                while True:
                
                # asking users for input

                    row, col = list(
                        map(int, input("Enter row and column numbers to fix a spot: ").split()))
                    print()

                    if self.board[row - 1][col - 1] != "-":
                        print("The spot cannot be fixed, fix another spot\n") 

                    else:
                        break

                # fixing the spot
                self.fix_spot(row - 1, col - 1, player)

                # checking if the current player has won or not
                if self.logic.is_player_win(player, self.board):
                    print(f"Player {player} wins the game!")
                    break
                    
                # checking whether the game is draw or not                  
                if self.logic.is_board_filled(self.board):
                    print("Match Draw!")
                    break
                
                # swapping the turn
                player = self.logic.swap_player_turn(player)
                
                # checking whether the game is draw or not                  
                if self.logic.is_board_filled(self.board):
                    print("Match Draw!")
                    break

            
        else:   
#                 self.show_board()
            while True:
                if computer_first == 1:
                    self.computer_move(computer)
                    if self.logic.is_player_win(computer, self.board):
                        print("You lose!")
                        break
                    
                    if self.logic.is_board_filled(self.board):
                        print("Match Draw!")
                        break

                    self.show_board()
                    print()
                    print("Your turn")

                    while True:
                        row, col = list(
                            map(int, input("Enter row and column numbers to fix a spot: ").split()))
                        print()

                        if self.board[row - 1][col - 1] != "-":
                            print("The spot cannot be fixed, fix another spot\n") 

                        else:
                            break

                    self.fix_spot(row - 1, col - 1, player)
                    if self.logic.is_player_win(player, self.board):
                        print("You win!")
                        break
                    
                    self.show_board()
                    print()

                else:
                    self.show_board()
                    print()
                    print("Your turn")

                    while True:
                        row, col = list(
                            map(int, input("Enter row and column numbers to fix a spot: ").split()))
                        print()

                        if self.board[row - 1][col - 1] != "-":
                            print("The spot cannot be fixed, fix another spot\n") 

                        else:
                            break

                    self.fix_spot(row - 1, col - 1, player)
                    self.show_board()
                    print()
                    if self.logic.is_player_win(player, self.board):
                        print("You win!")
                        break
                    
                    if self.logic.is_board_filled(self.board):
                        print("Match Draw!")
                        break

                    self.computer_move(computer)

                    if self.logic.is_player_win(computer, self.board):
                        print("You lose!")
                        break
                
        # showing the final view of board
        print()
        self.show_board()

if __name__ == '__main__':
    cli = Cli()
    cli.start()
