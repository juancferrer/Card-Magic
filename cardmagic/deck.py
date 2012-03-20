import random

from cardmagic.card import Card, VALID_SUITS, VALID_RANKS

class Deck(object):
    '''I contain a list of cards'''

    def __init__(self, cards=None, auto_create=True):
        '''Creates a Deck instance

        :arg cards: Holds the cards for this deck
        :type cards: List of Card objects

        :arg auto_create: To create a populated deck for you or not
        :type auto_create: boolean

        :rtype: None
        '''
        if not auto_create:
            self.cards = cards #list of cards already created
            return
        self.cards = []
        for rank in VALID_RANKS:
            for suit in VALID_SUITS:
                self.cards.append(Card(suit=suit, rank=rank))
    
    def shuffle(self, shuffle_method=random.shuffle, random=random.random):
        '''Shuffles this deck of cards

        :arg shuffle_method: Method used to shuffle the cards.
            This method should take 2 arguments.  A deck of cards to shuffle, 
            and a function that returns a random float [0.0, 1.0)
        :type shuffle_method: callable

        :arg random: Random method passed into the shuffle_method
        :type random: callable

        :rtype: None
        '''
        shuffle_method(self.cards, random)

