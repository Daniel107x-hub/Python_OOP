class Suit:

    SYMBOLS = {'Clubs': '♣', 'Diamonds': '♦', 'Hearts': '♥', 'Spades': '♠'}

    def __init__(self, description):
        self._description = description.capitalize().strip()
        self._symbol = Suit.SYMBOLS[self.description]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol
