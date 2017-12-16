# -*- coding: utf-8 -*-
from random import randint

max_number = 100
secret_number = randint(1, max_number)
guesses = 0
print "Guess the number between 1 and %s" % max_number
for i in range(100):
    guesses = guesses + 1
    guess = raw_input("Guess: ")
    if int(guess) == secret_number:
        print "Correct! Number of guesses: %s" % guesses
        break
    elif int(guess) > secret_number:
        print "Too high"
    else:
        print "Too low"
