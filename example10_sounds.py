# -*- coding: utf-8 -*-
import subprocess
from time import sleep

# Playing a sound, for example a sound effect on wrong answer.
subprocess.call(["afplay", "test_audio.m4a"])  # The file "test_audio.m4a" must be where the program is run from.

# Playing a song in the background while the program is running.
background_sound_process = subprocess.Popen(["afplay", "odpod-ringtone.mp3"])

for i in range(10):
    print i
    sleep(1)
background_sound_process.kill()
print "End"
