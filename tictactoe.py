class Solution(object):
    def tictactoe(self, moves):
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        
        def check_winner(player):
            # Check rows and columns
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        for i, (row, col) in enumerate(moves):
            player = 'A' if i % 2 == 0 else 'B'
            grid[row][col] = player
            
            if check_winner(player):
                return player
        
        if len(moves) == 9:
            return "Draw"
