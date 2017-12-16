# -*- coding: utf-8 -*-
from random import randint
from time import sleep
from datetime import datetime
import subprocess

MAX = 100
MAX_GUESSES = 8
secret = randint(1, MAX)


def ranking(max_number, guesses_used):
    if max_number <= 10:
        if guesses_used <= 2:
             return "Gold"
        elif guesses_used <= 4:
            return "Silver"
        else:
            return "Bronze"
    else:
        if guesses_used <= 4:
            return "Gold"
        elif guesses_used <= 7:
            return "Silver"
        else:
            return "Bronze"

name = raw_input("What is your name? ")
print "Hello %s" % name
print
print "Guess the number between 1 and %s" % MAX
print
sleep(3)
begin_time = datetime.now()
print "Start time: %s" % begin_time

already_guessed = []

for i in range(100):
    now = datetime.now()
    used_time = (now - begin_time).total_seconds()
    if used_time > 30:
        print "You took too long to guess."
        break

    guesses = i + 1
    guess = raw_input("Guess: ")
    guess = int(guess)
    if guess == secret:
        print
        print "Correct!! You used %s guesses." % guesses
        print "Your ranking %s: %s" % (name, ranking(MAX, guesses))
        break
    elif guess > secret:
        print "Too high"
    elif guess < secret:
        print "Too low"

    if guess in already_guessed:
        print "You already guessed that!"
    already_guessed.append(guess)

    if guesses >= MAX_GUESSES:
        print
        print "Too many guesses!! You used %s guesses." % guesses
        print "Your ranking %s: %s" % (name, ranking(MAX, guesses))
        break

print "Thank you for playing."
