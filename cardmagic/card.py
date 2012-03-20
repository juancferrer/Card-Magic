import gettext
import locale
import os

from cardmagic.exceptions import InvalidRankException, InvalidSuitException
gettext.install('cardmagic', 
        localedir=os.path.join(os.path.dirname(__file__),'translations'), 
        unicode=True)

# Ranks and suits from here: http://en.wikipedia.org/wiki/Playing_card#Styling
VALID_RANKS = range(1,14) # 1 - 13
VALID_SUITS = {0:_('Spades'), 1:_('Hearts'), 2:_('Diamonds'), 3:_('Clubs')}


class Card(object):
    ''' I am a playing card '''

    def __init__(self, rank=1, suit=0):
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

    def _get_encoding(self,):
        return locale.getdefaultlocale()[1] #'ISO8859-1', 'UTF-8', etc..

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
        return 'Card: %s %s' % (self.rank, VALID_SUITS[self.suit].encode(self._get_encoding()))

    def __unicode__(self,):
        return 'Card: %s %s' % (self.rank, VALID_SUITS[self.suit].encode(self._get_encoding()))
