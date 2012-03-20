import random

from cardmagic.deck import Deck

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print random.sample(deck, 7)
