# Based on a challenge from: https://openhatch.org/wiki/Flash_card_challenge
# Takes a tab-separated value file as the flashcard dictionary
# To run, type into a terminal, "python flashcards.py my_dict.tsv", where my_dict.tsv is a tab-separated value file located in the same folder as flashcards.py.

import random
from sys import argv

script, filename = argv

dictionary = open(filename, 'r')
cards = []
for line in dictionary:
    card = line.split('\t')
    cards.append(card)

print "================================================================================="
print "Welcome to the flashcards study aid. Type 'quit' at any time to exit the program."
print "================================================================================="

while True:
    random_card = random.choice(cards)
    print "\n%s" %random_card[1]
    ans = raw_input("\nWhat is the term being defined? (type 'give' to show the answer) > ")
    if ans.lower() == "quit":
        print "Goodbye."
        break
    elif ans.lower() == "give":
        print "The correct answer was %s." %random_card[0].upper()
        wrong = False
    elif ans.lower() == random_card[0]:
        print "%s is correct." %ans.upper()
        wrong = False
    else:
        print "%s is incorrect. Better luck on the next card." %ans.upper()