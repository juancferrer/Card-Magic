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
        self.assertRaises(InvalidRankException, Card, *(100, 'Spades'))

    def test_invalid_suit(self,):
        self.assertRaises(InvalidSuitException, Card, *(1, 'foo'))

if __name__ == '__main__':
    unittest.main()
