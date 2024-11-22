'''Card Deck Example'''
import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self): #special nethods - dunder methods
    self._cards = [Card(rank, suit) for suit in self.suits
                   for rank in self.ranks]
  def __len__(self):
    return len(self._cards)
  def __getitem__(self, position):
    return self._cards[position]
deck = FrenchDeck()
# print(len(deck)) - 52
# print(deck[-1]) - Card(rank='A', suit='hearts')
# print(choice(deck)) - random card
# print(deck[:3]) - first 3 cards
# print(deck[12::13]) - all aces; deck[12::13] starts at the 13th card and selects every 13th card thereafter
# for card in reversed(deck):
#   print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
# print(spades_high(Card('3','spades'))) # 1*4+3 = 7
for card in sorted(deck, key=spades_high):
    print(card)
