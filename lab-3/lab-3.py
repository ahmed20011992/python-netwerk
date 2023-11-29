

import random


class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13

        self._suit = suit
        self._value = value

    def getValue(self):
        return self._value

    def getSuit(self):
        return self._suit

    def __str__(self):
        values = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                  7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
        suits = {1: 'Hearts', 2: 'Diamonds', 3: 'Clubs', 4: 'Spades'}

        value_name = values[self._value]
        suit_name = suits[self._suit]

        return f"{value_name} of {suit_name}"


class CardDeck:
    def __init__(self):
        self._cards = []
        self.reset()

    def shuffle(self):
        random.shuffle(self._cards)

    def getCard(self):
        if not self._cards:
            return None
        return self._cards.pop()

    def size(self):
        return len(self._cards)

    def reset(self):
        suits = list(range(1, 5))
        values = list(range(1, 14))
        self._cards = [Card(suit, value) for suit in suits for value in values]
        self.shuffle()


deck = CardDeck()
deck.shuffle()


while deck.size() > 0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))
