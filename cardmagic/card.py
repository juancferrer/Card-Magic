from cardmagic.exceptions import InvalidRankException, InvalidSuitException

# Ranks and suits from here: http://en.wikipedia.org/wiki/Playing_card#Styling
VALID_RANKS = range(1,14) # 1 - 13
VALID_SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

class Card(object):
    ''' I am a playing card '''

    def __init__(self, rank=1, suit='Spades'):
        ''' Creates a card instance

        :arg rank: The rank for this card
        :type rank: int

        :arg suit: The suit for this card
        :type suit: basestring

        :rtype: None

        :raises InvalidRankException: The given rank is invalid
        :raises InvalidSuitException: The  given suit is invalid
        '''
        if not rank in VALID_RANKS:
            raise InvalidRankException()
        if not suit in VALID_SUITS:
            raise InvalidSuitException()
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank 

    def __gt__(self, other):
        return self.rank > other.rank 

    def __ge__(self, other):
        return self.rank >= other.rank 

    def __le__(self, other):
        return self.rank <= other.rank 

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self,):
        return 'Card: %s %s' % (self.rank, self.suit)

    def __unicode__(self,):
        return 'Card: %s %s' % (self.rank, self.suit)
