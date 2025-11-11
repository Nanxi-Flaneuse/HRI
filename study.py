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


# tips = {"eyes":"Do you want to relax your eyes? You can look at something 20 feet away for 20 seconds!","cross":"I know a good strech! Cross your legs and touch your toes, then slowly come up, verterbrate by verterbrate!","shake":"Shake your arms and legs and loosen your muscle!","yoga":"You can get on the floor and do some baby pose to strech your back!"}
# tip = np.random.choice(list(tips.keys()), 1)
# print(tip[0])
# print(tips[tip[0]])
activities = [0,1,2,3]
keys = list(tips.keys())
toy = scanner.find_toy(toy_name="SB-69F1")
# async def main():
#     # toy = scanner.find_toy(toy_name="SB-69F1")
#     async with SpheroEduAPI(toy) as droid:

#         random.shuffle(activities)
#         activity_order = activities[:]
#         i = 0
#         while True:
#             time.sleep(2)
#             # await asyncio.sleep(5)
#             speak("It is time to take a break, let's get up and stretch")
#             tip = keys[activity_order[i]]
#             speak(tips[tip])

#             # social group
#             # time.sleep(2)
#             await asyncio.sleep(2)
#             if tip == 'eyes':
#                 eyes()
#             elif tip == 'cross':
#                 cross(droid)
#             elif tip == "shake":
#                 shake(droid)
#             elif tip == 'yoga':
#                 yoga()
#             # speak("I will play some background music for you while you stretch!")
#             # play music
#             speak("Now let's get back to work!")

#             # # physical group
#             # time.sleep(2)
#             # if tip == 'eyes':
#             #     speak("You can juggle me around and focus your attention on me! That will also be a good exercise for your eyes")
#             #     # Sphero makes sound when being juggled
#             # elif tip == 'cross':
#             #     speak("Let's play chase! I will run around the room now and you'll come and get me!")
#             #     # Sphero runs around
#             # elif tip == "shake":
#             #     speak("Shake me up and down with your left hand! Am I heavy?")
#             #     # makes sound when shaken
#             #     speak("Now do the same with your right hand!")
#             #     # makes sound when shaken
#             # elif tip == "yoga":
#             #     speak("As you relax, you can also roll me around with your hands! Feel my weight and the texture of my shell. Am I heavy or light? What's the texture of my shell?")


#             if i == 3:
#                 i = 0
#             else:
#                 i += 1


#     # spin(360, 0.6)
# asyncio.run(main())


with SpheroEduAPI(toy) as droid:

    random.shuffle(activities)
    activity_order = activities[:]
    i = 0
    while True:
        time.sleep(1200)
        # await asyncio.sleep(5)
        speak("It is time to take a break, let's get up and stretch")
        tip = keys[activity_order[i]]
        speak(tips[tip])

        # social group
        time.sleep(1)
        if tip == 'eyes':
            eyes()
        elif tip == 'cross':
            cross(droid)
        elif tip == "shake":
            shake(droid)
        elif tip == 'yoga':
            yoga()
        # speak("I will play some background music for you while you stretch!")
        # play music
        speak("Now let's get back to work!")

        # # physical group
        # time.sleep(2)
        # if tip == 'eyes':
        #     speak("You can juggle me around and focus your attention on me! That will also be a good exercise for your eyes")
        #     # Sphero makes sound when being juggled
        # elif tip == 'cross':
        #     speak("Let's play chase! I will run around the room now and you'll come and get me!")
        #     # Sphero runs around
        # elif tip == "shake":
        #     speak("Shake me up and down with your left hand! Am I heavy?")
        #     # makes sound when shaken
        #     speak("Now do the same with your right hand!")
        #     # makes sound when shaken
        # elif tip == "yoga":
        #     speak("As you relax, you can also roll me around with your hands! Feel my weight and the texture of my shell. Am I heavy or light? What's the texture of my shell?")


        if i == 3:
            i = 0
        else:
            i += 1