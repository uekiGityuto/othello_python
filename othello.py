from enum import Enum


class Color(Enum):
    WHITE = -1
    BLACK = 1


class Stone:
    def __init__(self, color: Color) -> None:
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
    def __init__(self, color: Color = None) -> None:
        if color is None:
            self.stone = None
        else:
            self.stone = Stone(color)

    def put(self, color: Color) -> None:
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


class Address:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Board:
    def __init__(self) -> None:
        self.board = [[Cell() for i in range(8)] for i in range(8)]
        self.board[3][3].put(Color.BLACK)
        self.board[3][4].put(Color.WHITE)
        self.board[4][3].put(Color.WHITE)
        self.board[4][4].put(Color.BLACK)

    def draw(self) -> None:
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(i, end="")
            for cell in row:
                cell.draw()
            print("|")

    def put(self, x: int, y: int, color: Color) -> bool:
        self.board[x][y].put(color)
        return True


class Controller:
    def __init__(self, turn: Color) -> None:
        self.turn = turn
        self.board = Board()

    def change_trun(self) -> None:
        if self.turn == Color.WHITE:
            self.turn = Color.BLACK
        else:
            self.turn = Color.WHITE

    def validate(self, inputs: list[str]) -> bool:
        x = inputs[0]
        y = inputs[1]
        if x.isdecimal() and 0 <= int(x) < 7 and y.isdecimal() and 0 <= int(y) <= 7:
            return True
        else:
            return False

    def start(self) -> None:
        print("石を置きたい場所を「列番号,行番号」の形式で入力して下さい。例）左上隅の場合：0,0")
        print("やめたい時は「quit」と入力して下さい。")
        print("パスをしたい時は「pass」と入力して下さい。")

        while True:
            print("白の番です。" if self.turn == Color.WHITE else "黒の番です。")
            self.board.draw()
            input_str = input("> ")
            if input_str == "quit":
                break
            if input_str == "pass":
                print("パスします。")
                self.change_trun()
                continue
            inputs = [str.strip() for str in input_str.split(",")]
            if not self.validate(inputs):
                print("入力内容が不正です。「列番号,行番号」の形式で入力して下さい。例）左上隅の場合：0,0")
                continue
            if not self.board.put(int(inputs[0]), int(inputs[1]), self.turn):
                print("そこには置けません。")
                continue
            self.turn = self.change_trun()

        print("終了します。")


if __name__ == "__main__":
    ctrl = Controller(Color.WHITE)
    ctrl.start()
