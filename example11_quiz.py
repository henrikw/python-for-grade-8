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

correct = []
wrong = []
question_number = 0
for question in questions:
    question_number = question_number + 1
    print "%s: %s" % (question_number, question.get("question"))
    print
    for letter in ("a", "b", "c"):
        print "%s: %s" % (letter, question.get(letter))
    print
    answer = raw_input("Pick a, b or c: ")
    if answer == question.get("correct"):
        correct.append(question_number)
        print "Correct"
    else:
        wrong.append(question_number)
        print "Wrong"
    sleep(2)
    print

print "Results: %s correct answers (%s), %s wrong answers (%s)" %\
      (len(correct), correct, len(wrong), wrong)
print
