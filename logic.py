import random

class Logic:

    def __init__(self):
        pass

    def get_random_first_player(self):
        return random.randint(0, 1)


    def is_player_win(self, player, board):
        win = None

        n = len(board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    def is_board_filled(self, board):
        for row in board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
