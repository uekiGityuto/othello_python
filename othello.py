from enum import Enum


class Color(Enum):
    WHITE = -1
    BLACK = 1


def reverse_color(color):
    return Color.WHITE if color == Color.BLACK else Color.BLACK


class Stone:
    def __init__(self, color) -> None:
        self.color = color

    def get(self) -> str:
        if self.color == Color.WHITE:
            return "o"
        else:
            return "●"

    def is_black(self) -> bool:
        return True if self.color == Color.BLACK else False

    def is_white(self) -> bool:
        return True if self.color == Color.WHITE else False

    def reverse(self) -> None:
        if self.color == Color.WHITE:
            self.color = Color.BLACK
        else:
            self.color = Color.WHITE


class Cell:
    def __init__(self, color = None) -> None:
        if color is None:
            self.stone = None
        else:
            self.stone = Stone(color)

    def put(self, color) -> None:
        self.stone = Stone(color)

    def draw(self) -> None:
        stone = " " if self.stone is None else self.stone.get()
        print(f"|{stone}", end="")

    def reverse(self) -> None:
        if not self.stone is None:
            self.stone.reverse()

    def is_none(self) -> bool:
        return self.stone is None

    def is_white(self) -> bool:
        if self.is_none():
            return False
        else:
            return self.stone.is_white()

    def is_black(self) -> bool:
        if self.is_none():
            return False
        else:
            return self.stone.is_black()


class Board:
    def __init__(self) -> None:
        self.board = [[Cell() for i in range(8)] for i in range(8)]
        self.board[3][3].put(Color.BLACK)
        self.board[3][4].put(Color.WHITE)
        self.board[4][3].put(Color.WHITE)
        self.board[4][4].put(Color.BLACK)


    def draw(self) -> None:
        print('  0 1 2 3 4 5 6 7')
        for i, row in enumerate(self.board):
            print(i, end="")
            for cell in row:
                cell.draw()
            print('|')


print("石を置きたい場所を「列番号,行番号」の形式で入力して下さい。例）左上隅の場合：0,0")
print("やめたい時は「quit」と入力して下さい。")
print("パスをしたい時は「pass」と入力して下さい。")

turn = Color.WHITE
print("白の番です。" if turn == Color.WHITE else "黒の番です。")
board = Board()
board.draw()

input_str = ""
while input_str != "quit":
    # 文字を入力する
    input_str = input("> ")
    print(f"入力した文字列は{input_str}です。")
    if input_str == "pass":
        break
    turn = reverse_color(turn)
    print("白の番です。" if turn == Color.WHITE else "黒の番です。")
    board.draw()

print("終了しました")
