import random

from .card import Card, VALID_SUITS, VALID_RANKS

class Deck(object):
    def __init__(self, cards=None, auto_create=True):
        if not auto_create:
            self.cards = cards #list of cards already created
            return
        self.cards = []
        for rank in VALID_RANKS:
            for suit in VALID_SUITS:
                self.cards.append(Card(suit=suit, rank=rank))
    
    def shuffle(self, shuffle_method=random.shuffle, random=random.random):
        shuffle_method(self.cards, random)

