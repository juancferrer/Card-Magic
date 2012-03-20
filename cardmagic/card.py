from .exceptions import InvalidRankException, InvalidSuitException

# Ranks and suits from here: http://en.wikipedia.org/wiki/Playing_card#Styling
VALID_RANKS = range(1,14) # 1 - 13
VALID_SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

class Card(object):
    def __init__(self, rank=1, suit='Spades'):
        if not rank in VALID_RANKS:
            raise InvalidRankException()
        if not suit in VALID_SUITS:
            raise InvalidSuitException()
        self.rank = rank
        self.suit = suit

    def __repr__(self,):
        return 'Card: %s %s' % (self.rank, self.suit)

    def __unicode__(self,):
        return 'Card: %s %s' % (self.rank, self.suit)
