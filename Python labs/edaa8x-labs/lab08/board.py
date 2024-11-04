class TicTacToeBoard:
    
    def __init__(self) -> None:
        self._board = [['-'for _ in range(3)] for _ in range(3)]
    
    def get(self, row: int, col: int) -> str:
        return self._board[row][col]
    
    def is_empty(self, row: int, col: int) -> bool:
        if self._board[row][col] == '-':
            return True
        else:
            return False

    def place(self, marker: str, row: int, col: int) -> bool:
        if self.is_empty(row, col):
            self._board[row][col] = marker
            return True
        else:
            return False

    def is_full(self):
        for row in self._board:
            for col in row:
                if col == '-':
                    return False

        return True
    
    
    def is_winner(self, marker: str) -> bool:
        
        for row in self._board:
            if all(cell == marker for cell in row):
                return True
            
        
        for col in range(3):
            if all(self._board[row][col] for row in range(3)):
                return True
        
        
        if all(self._board[i][i] == marker for i in range(3)):    
            return True
        if all(self._board[i][2 - i] == marker for i in range(3)):
            return True
        
        
        
        return False
        
        
    def restart(self):
        self.__init__()
        
        
    def print_board(self):
        for row in self._board:
            print(' '.join(row))
    
    


if __name__ == '__main__':
    b = TicTacToeBoard()
    b.place('X', 0, 0)
    b.place('X', 0, 1)
    b.place('X', 0, 2)
    b.print_board()
    


