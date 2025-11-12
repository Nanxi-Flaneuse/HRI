import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from gtts import gTTS
import os
from utils import *
import numpy as np
from sphero_activities import *
import random
import asyncio

def main(behavior = 'social'):
    activities = [0,1,2,3]
    keys = list(tips.keys())
    toy = scanner.find_toy(toy_name="SB-69F1")
    with SpheroEduAPI(toy) as droid:
        # randomly shuffle the order of activities
        random.shuffle(activities)
        activity_order = activities[:]
        i = 0
        while True:
            time.sleep(1200)
            # await asyncio.sleep(5)
            speak("It is time to take a break, let's get up and stretch")
            # pick an activity
            tip = keys[activity_order[i]]
            speak(tips[tip])
            if behavior == 'social':
                # social group
                time.sleep(1)
                if tip == 'eyes':
                    eyes(droid,behavior)
                elif tip == 'cross':
                    cross(droid,behavior)
                elif tip == "shake":
                    shake(droid,behavior)
                elif tip == 'yoga':
                    yoga(droid,behavior)
                

            # # physical group - actually will be implemented in sphero_activities.py
            elif behavior == 'physical':
                time.sleep(2)
                if tip == 'eyes':
                    speak("You can juggle me around and focus your attention on me! That will also be a good exercise for your eyes")
                    # Sphero makes sound when being juggled
                elif tip == 'cross':
                    speak("Let's play chase! I will run around the room now and you'll come and get me!")
                    # Sphero runs around
                elif tip == "shake":
                    speak("Shake me up and down with your left hand! Am I heavy?")
                    # makes sound when shaken
                    speak("Now do the same with your right hand!")
                    # makes sound when shaken
                elif tip == "yoga":
                    speak("As you relax, you can also roll me around with your hands! Feel my weight and the texture of my shell. Am I heavy or light? What's the texture of my shell?")

            speak("Now let's get back to work!")
            if i == 3:
                i = 0
            else:
                i += 1

if __name__ == '__main__':
    main()