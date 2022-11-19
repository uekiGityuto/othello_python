from enum import Enum
from typing import Callable, List, Optional


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
    def __init__(self, color: Optional[Color] = None) -> None:
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
        if self.stone is None:
            return False
        else:
            return self.stone.is_white()

    def is_black(self) -> bool:
        if self.stone is None:
            return False
        else:
            return self.stone.is_black()


class Address:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_valid(self) -> bool:
        if 0 <= self.x <= 7 and 0 <= self.y <= 7:
            return True
        else:
            return False


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

    def put(self, color: Color, address: Address) -> bool:
        targets = self.search(color, address)
        if len(targets) == 0:
            return False

        self.ref_cell(address).put(color)
        for t in targets:
            self.ref_cell(t).reverse()
        return True

    def count_black(self) -> int:
        count = 0
        for row in self.board:
            for cell in row:
                count += 1 if cell.is_black() else 0
        return count

    def count_white(self) -> int:
        count = 0
        for row in self.board:
            for cell in row:
                count += 1 if cell.is_white() else 0
        return count

    def ref_cell(self, address: Address) -> Cell:
        return self.board[address.y][address.x]

    def search(self, turn: Color, startPoint: Address) -> List[Address]:
        def search_next(
            current: Address, list: List[Address], next: Callable[[Address], Address]
        ) -> List[Address]:
            next_address = next(current)
            if not next_address.is_valid:
                return []
            next_cell = self.ref_cell(next_address)
            if next_cell.is_none():
                return []
            if (next_cell.is_black() and turn == Color.WHITE) or (
                next_cell.is_white() and turn == Color.BLACK
            ):
                list.append(next_address)
                return search_next(next_address, list, next)
            return list

        results: List[Address] = []
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x, address.y - 1)
            )
        )
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x, address.y + 1)
            )
        )
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x - 1, address.y)
            )
        )
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x + 1, address.y)
            )
        )

        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x - 1, address.y - 1)
            )
        )
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x + 1, address.y - 1)
            )
        )
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x - 1, address.y + 1)
            )
        )
        results.extend(
            search_next(
                startPoint, [], lambda address: Address(address.x + 1, address.y + 1)
            )
        )
        return results
