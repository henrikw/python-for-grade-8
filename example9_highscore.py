# -*- coding: utf-8 -*-
import pickle
import os.path

HIGHSCORE_FILE_NAME = 'saved_score.txt'

# Check if there is a file with name HIGHSCORE_FILE_NAME.
if os.path.isfile(HIGHSCORE_FILE_NAME):
    # The file already exists, so read what is stored in it.
    score = pickle.load(open(HIGHSCORE_FILE_NAME, 'r'))
else:
    # Create an empty dict
    score = {}

# We can update/add new points.
score['Emil'] = 15.4
score['Fia'] = 102
score['Amanda'] = 33

# Values in a dict are not ordered.
print score

# We can find the highest value (who has the highest score) like this:
highest_score = -1
highest_name = None  # No name yet.
for namn in score.keys():
    if score[namn] > highest_score:
        highest_score = score[namn]
        highest_name = namn

print "Highest score: %s has %s" % (highest_name, highest_score)

# Save the score in the file.
pickle.dump(score, open(HIGHSCORE_FILE_NAME, 'w'))

# The next time this program is run, we will read from the file that the dict is saved in.
