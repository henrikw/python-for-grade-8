import subprocess
from time import sleep
from datetime import datetime
from random import randint 

def ranking(guesses):
    if guesses < 4:
        return "Gold"
    elif guesses > 3 and guesses < 8:
        return "Silver"
    else:
        return "Bronze"

def time_ranking(time_taken):
    if time_taken < 15:
        return "Excellent, that was quick"
    elif time_taken > 15 and time_taken < 30:
        return "Good job, you were fast"
    elif time_taken > 30 and time_taken < 45:
        return "Pretty good speed, but you could go faster"
    else:
       return "Better luck next time with the time"

for i in range(999999): 

    lista = []

    most = 100

    secret = randint(1,most+1)

    #secret = 5

    previous_guess = -421414352465477867536425134414

    name = raw_input("What is your name? ")
    sleep (0.6)
    print
    print "Welcome to the guessing game %s." % name
    sleep(1)
    print
    print "Guess a number between 1 and %s, please." % most 
    print

    begin_time = datetime.now()

    for i in range(most+1):
        sleep(0.6)
        guess = raw_input("Type in your guess: ")
        guess = int(guess)
        current_guess = guess
        current_guess = int(guess)

        if current_guess in lista:
            print "You have already guessed that"
            subprocess.call(["afplay", "Wrong Buzzer Sound Effect.m4a"])
        lista.append(guess)       
        
        if guess == secret:
            print
            print "Correct, you got %s, %s" % (ranking(i+1), name)
            end_time = datetime.now()
            time_taken = (end_time - begin_time).total_seconds()
            time_taken = int(round(time_taken))
            subprocess.call(["afplay", "Ding Sound Effect.m4a"])
            print

            if i+1 == 1:
                print "Wow it only took you 1 guess" 

            else:
                print "It took you %s guesses, %s" % (i+1, name)
            print
            sleep(0.6)
            print "%s, it took you %s seconds." % (time_ranking(time_taken), time_taken)
            print
            break
        
        elif i+1 == most:
            print
            print "Are you stupid how havent you guessed it already. The anwser was %s!" % (secret)
            print
            break
        
        if guess == previous_guess:
            print "Don't you remember, it was your last guess"
            sleep(0.6)
        previous_guess = guess
        
        if guess > most:
            print "I've told you already. You can only guess between 1 and %s" % most
            subprocess.call(["afplay", "Wrong Buzzer Sound Effect.m4a"])

        if guess < 1:
            print "I've told you already. You can only guess between 1 and %s" % most
            subprocess.call(["afplay", "Wrong Buzzer Sound Effect.m4a"])

            
        elif guess - secret > 0 and guess - secret < 6:
            print "A little too high"
        elif secret - guess > 0 and secret - guess < 6:
            print "A little too low"
        elif guess > secret:
            print "Too high"
        elif guess < secret:
            print "Too low"
    sleep(1)        
    igen = raw_input("Do you want to play again? Press 1 for yes and 2 for no. ") 
    igen = int(igen)
    
    if igen == 2:
        print
        print "Ok, maybe another time"
        print
        break

    elif igen == 1:
        print
        print "Great"
        print 
        pass




