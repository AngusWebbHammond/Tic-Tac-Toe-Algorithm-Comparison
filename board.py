class Board:
    def __init__(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def move(self, pos: list[int, int], piece: str):
        self.board[pos[0]][pos[1]] = piece

    def check_win(self) -> tuple[bool, str | None, str | None]:
        for index in range(3):
            for piece in ["X", "O"]:
                check_win = self.check_piece_win(index, piece)
                if check_win[0]:
                    return (True, piece, check_win[1])
        return (False, None, None)

    def check_piece_win(self, index: int, piece: str) -> tuple[bool, str | None]:
        piece_win = [piece, piece, piece]
        if piece_win == self.board[index]:
            return (True, "HORIZONTAL")
        if piece_win == [
            self.board[0][index],
            self.board[1][index],
            self.board[2][index],
        ]:
            return (True, "VERTICAL")
        if piece_win == [self.board[0][0], self.board[1][1], self.board[2][2]]:
            return (True, "DIAGONALLEFT")
        if piece_win == [self.board[0][2], self.board[1][1], self.board[2][0]]:
            return (True, "DIAGONALRIGHT")
        return (False, None)

    def print_board(self):
        print(self.board[i][j] for i in range(3) for j in range(3))

    def clear_board(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
