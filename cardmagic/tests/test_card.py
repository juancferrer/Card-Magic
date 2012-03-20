import unittest

from cardmagic.card import Card, VALID_SUITS, VALID_RANKS 
from cardmagic.exceptions import InvalidRankException, InvalidSuitException

class CardTests(unittest.TestCase):
    def setUp(self,):
        pass

    def test_valid_card(self,):
        for suit in VALID_SUITS:
            for rank in VALID_RANKS:
                c = Card(rank, suit)
                self.assertIsInstance(c, Card)
                self.assertEqual(c.rank, rank)
                self.assertEqual(c.suit, suit)

    def test_invalid_rank(self,):
        self.assertRaises(InvalidRankException, Card, *(100, 0))

    def test_invalid_suit(self,):
        self.assertRaises(InvalidSuitException, Card, *(1, 'foo'))

    def test_eq(self,):
        c1 = Card(1, 0)
        c2 = Card(1, 0)
        self.assertEqual(c1, c2)

    def test_lt(self,):
        c1 = Card(1, 0)
        c2 = Card(2, 0)
        self.assertLess(c1, c2)

    def test_le(self,):
        c1 = Card(1, 0)
        c2 = Card(2, 0)
        self.assertLessEqual(c1, c2)
        c2 = Card(1, 0)
        self.assertLessEqual(c1, c2)

    def test_gt(self,):
        c1 = Card(3, 0)
        c2 = Card(2, 0)
        self.assertGreater(c1, c2)

    def test_ge(self,):
        c1 = Card(3, 0)
        c2 = Card(2, 0)
        self.assertGreaterEqual(c1, c2)
        c2 = Card(2, 0)
        self.assertGreaterEqual(c1, c2)

    def test_ne(self,):
        c1 = Card(3, 0)
        c2 = Card(2, 0)
        self.assertNotEqual(c1, c2)
        c2 = Card(3, 1)
        self.assertNotEqual(c1, c2)

if __name__ == '__main__':
    unittest.main()
