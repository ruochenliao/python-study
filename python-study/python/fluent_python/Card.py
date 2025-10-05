import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
l = len(deck)
print(l)
random_card = choice(deck)
print(random_card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# 牌面大小按照点数（A最大），以及黑桃、红心、方块、梅花的顺序排列
sorted_cards = sorted(deck, key=spades_high)
print(sorted_cards)

temp_list = ["a", "b", "c"]
index = temp_list.index("b")
print(index)

