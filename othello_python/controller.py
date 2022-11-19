from othello_python import model


class Controller:
    def __init__(self, turn: model.Color) -> None:
        self.turn = turn
        self.board = model.Board()

    def change_trun(self) -> None:
        if self.turn == model.Color.WHITE:
            self.turn = model.Color.BLACK
        else:
            self.turn = model.Color.WHITE

    def validate(self, input_str: str) -> bool:
        inputs = [str.strip() for str in input_str.split(",")]
        if len(inputs) != 2:
            return False
        x, y = inputs
        if x.isdecimal() and 0 <= int(x) <= 7 and y.isdecimal() and 0 <= int(y) <= 7:
            return True
        else:
            return False

    def start(self) -> None:
        print("石を置きたい場所を「列番号,行番号」の形式で入力して下さい。例）左上隅の場合：0,0")
        print("やめたい時は「quit」と入力して下さい。")
        print("パスをしたい時は「pass」と入力して下さい。")

        while True:
            print("白の番です。" if self.turn == model.Color.WHITE else "黒の番です。")
            self.board.draw()
            input_str = input("> ")
            if input_str == "quit":
                break
            if input_str == "pass":
                print("パスします。")
                self.change_trun()
                continue
            if not self.validate(input_str):
                print("入力内容が不正です。「列番号,行番号」の形式で入力して下さい。例）左上隅の場合：0,0")
                continue
            x, y = [str.strip() for str in input_str.split(",")]
            address = model.Address(int(x), int(y))
            if not self.board.put(self.turn, address):
                print("そこには置けません。")
                continue
            self.change_trun()

        self.end()

    def end(self) -> None:
        black_num = self.board.count_black()
        white_num = self.board.count_white()
        print(f"白: {black_num}")
        print(f"黒: {white_num}")
        if white_num > black_num:
            print("白の勝利です。")
        elif black_num > white_num:
            print("黒の勝利です。")
        else:
            print("引き分けです。")


if __name__ == "__main__":
    ctrl = Controller(model.Color.WHITE)
    ctrl.start()
