import unittest

from othello_python.model import Color, Stone


class TestStone(unittest.TestCase):
    def test_get(self):
        white_stone = Stone(Color.WHITE)
        self.assertEqual(white_stone.get(), "o")
        black_stone = Stone(Color.BLACK)
        self.assertEqual(black_stone.get(), "●")

    def test_is_black(self):
        white_stone = Stone(Color.WHITE)
        self.assertFalse(white_stone.is_black())
        black_stone = Stone(Color.BLACK)
        self.assertTrue(black_stone.is_black())

    def test_is_white(self):
        white_stone = Stone(Color.WHITE)
        self.assertTrue(white_stone.is_white())
        black_stone = Stone(Color.BLACK)
        self.assertFalse(black_stone.is_white())

    def test_reverse(self):
        stone = Stone(Color.WHITE)
        stone.reverse()
        self.assertEqual(stone.get(), "●")
        stone.reverse()
        self.assertEqual(stone.get(), "o")
