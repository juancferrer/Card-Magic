import unittest
from collections import defaultdict

from cardmagic.card import Card, VALID_SUITS, VALID_RANKS 
from cardmagic.deck import Deck

class DeckTests(unittest.TestCase):
    def setUp(self,):
        pass

    def test_default(self,):
        deck = Deck()
        # Make sure there's 52 cards
        self.assertEqual(len(deck.cards), 52)
        # Make sure that there's only one of each card
        counter = defaultdict(list) # {'sui1': [1,2,3,..13], 'suit2': [...]}
        for card in deck.cards:
            counter[card.suit].append(card.rank)
        for suit,values in counter.iteritems():
            self.assertTrue(suit in VALID_SUITS)
            self.assertEqual(len(values), len(VALID_RANKS))
            for value in values:
                self.assertTrue(value in VALID_RANKS)

    def test_notauto_create(self,):
        deck = Deck(auto_create=False)
        self.assertFalse(deck.cards)

    def test_default_shuffle(self,):
        deck = Deck()
        copy = deck.cards[:]
        deck.shuffle()
        # Make sure all the card are still there
        for card in deck.cards:
            self.assertTrue(card in copy)
        # Did they actually get shuffled?
        for i,card in enumerate(deck.cards):
            if card != copy[i]:
                break # yay, not the same (i != 52)
        if i+1 == len(deck.cards):
            self.fail('Not shuffled')

    def test_custom_shuffle_notreally(self,):
        deck = Deck()
        copy = deck.cards[:]
        deck.shuffle(lambda deck,random: None,) # Don't really shuffle
        # Make sure all the card are still there
        for card in deck.cards:
            self.assertTrue(card in copy)
        # Are they in the same order too??
        for card,copied in zip(deck.cards, copy):
            self.assertEqual(card.rank, copied.rank)
            self.assertEqual(card.suit, copied.suit)

    def test_shuffle_random(self,):
        deck1 = Deck()
        deck2 = Deck()
        # Same initial state, same random seed...same outcome
        deck1.shuffle(random=lambda:0.5)
        deck2.shuffle(random=lambda:0.5)
        for card1, card2 in zip(deck1.cards, deck2.cards):
            self.assertEqual(card1.rank, card2.rank)
            self.assertEqual(card1.suit, card2.suit)
        
if __name__ == '__main__':
    unittest.main()
