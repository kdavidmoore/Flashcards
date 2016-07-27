# Based on a challenge from: https://openhatch.org/wiki/Flash_card_challenge
# Takes a tab-separated value file as the flashcard dictionary.
# Why? Because I was studying for the FG Exam and needed commas in my definitions.
# To run, type into a terminal, "python flashcards.py my_dict.tsv",
# where my_dict.tsv is a tab-separated value file located in the same folder as flashcards.py.
# This program would be more pythonic if python dictionaries were used instead of arrays.

import random
from sys import argv
script, filename = argv

cards = []
cardsRight = 0
cardsTotal = 0

dictionary = open(filename, 'r')
for line in dictionary:
	card = line.split('\t')
	cards.append(card)
print "=================================================================================="
print "Welcome to the flashcards study aid. Enter 'quit' at any time to exit the program."
print "=================================================================================="
while True:
	random_card = random.choice(cards)
	print "\n%s" %random_card[1]
	ans = raw_input("What is the term being defined? (enter 'give' to show the answer) > ")
	if ans.lower() == "quit":
		print "Quitting..."
 		break
	elif ans.lower() == "give":
		print "The correct answer was %s. Next card..." %random_card[0].upper()
		cardsTotal += 1
	elif ans.lower() == random_card[0]:
		print "%s is correct. Next card..." %ans.upper()
		cardsRight += 1
		cardsTotal += 1
	else:
		print "%s is incorrect. Next card..." %ans.upper()
		cardsTotal += 1
print "\nYou scored %s out of %s cards correctly." %(cardsRight, cardsTotal)
