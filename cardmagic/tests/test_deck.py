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
        self.assertEqual(len(deck), 52)
        # Make sure that there's only one of each card
        counter = defaultdict(list) # {'sui1': [1,2,3,..13], 'suit2': [...]}
        for card in deck:
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
        copy = deck[:]
        deck.shuffle()
        # Make sure all the card are still there
        for card in deck:
            self.assertTrue(card in copy)
        # Did they actually get shuffled?
        for i,card in enumerate(deck):
            if card != copy[i]:
                break # yay, not the same (i != 52)
        if i+1 == len(deck):
            self.fail('Not shuffled')

    def test_custom_shuffle_notreally(self,):
        deck = Deck()
        copy = deck[:]
        deck.shuffle(lambda deck,random: None,) # Don't really shuffle
        # Make sure all the card are still there
        for card in deck.cards:
            self.assertTrue(card in copy)
        # Are they in the same order too??
        for card,copied in zip(deck, copy):
            self.assertEqual(card, copied)

    def test_shuffle_random(self,):
        deck1 = Deck()
        deck2 = Deck()
        # Same initial state, same random seed...same outcome
        deck1.shuffle(random=lambda:0.5)
        deck2.shuffle(random=lambda:0.5)
        for card1, card2 in zip(deck1, deck2):
            self.assertEqual(card1, card2)

    def test_len(self,):
        deck = Deck()
        self.assertEqual(len(deck), len(deck.cards))
        deck.cards = []
        self.assertEqual(len(deck), len(deck.cards))

    def test_getitem(self,):
        deck = Deck()
        cards = [Card(1, 2), Card(2,0), Card(3,1)]
        deck.cards = cards
        self.assertEqual(deck[0], cards[0]) # Direct access
        self.assertEqual(deck[1], cards[1]) # Direct access
        self.assertEqual(deck[:2], cards[:2]) # slices
        self.assertEqual(deck[0::2], cards[0::2]) # slices with steps

    def test_iter(self,):
        deck = Deck()
        for i,card in enumerate(deck):
            pass
        self.assertEqual(i+1, len(deck))

        
if __name__ == '__main__':
    unittest.main()
