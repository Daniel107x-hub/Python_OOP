from Card import Card
from Suit import Suit
import random


class Deck:

    def __init__(self, is_empty=False):
        self._cards = []
        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for i in range(2, 15):
            for key in Suit.SYMBOLS:
                card = Card(Suit(key), i)
                self._cards.append(card)

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        self._cards.insert(0, card)
