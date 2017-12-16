# -*- coding: utf-8 -*-
from time import sleep

questions = [
    {"question": "What is the capital of Sweden?",
     "a": "Stockholm",
     "b": "Oslo",
     "c": "Göteborg",
     "correct": "a"},
    
    {"question": "What is 2 + 2?",
     "a": "3",
     "b": "5",
     "c": "4",
     "correct": "c"},
]        
    
for question in questions:
    print question.get("question")
    print
    for letter in ("a", "b", "c"):
        print "%s: %s" % (letter, question.get(letter))
    print
    answer = raw_input("Pick a, b or c: ")
    if answer == question.get("correct"):
        print "Correct"
    else:
        print "Wrong"
    sleep(2)
    print

