#!/usr/bin/env python
import sys
import re

class Card:
    def __init__(self, winning, ours, quantity=1):
        self.winning = winning
        self.ours = ours
        self.quantity = quantity

    def add_card(self):
        self.quantity += 1

    def find_wins(self):
        wins = 0
        for num in self.ours:
            if num in self.winning:
                wins += 1
        return wins

filename = sys.argv[1]
cards = []
# create cards
with open(filename, 'r') as input:
    for line in input:
        # split the line into sections and then numbers
        _, winning_nums, our_nums = re.split(r':|\|', line)
        winning_nums = winning_nums.split()
        our_nums = our_nums.split()
        cards.append(Card(winning_nums, our_nums))

# find quantities
result = 0
for i, card in enumerate(cards):
    wins = card.find_wins()
    for won_card in range(1, wins + 1):
        cards[i + won_card].quantity += card.quantity
        # "Cards will never make you copy a card past the end of the table"
        # (no need to worry about bounds)
    result += card.quantity
print(result)
