import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from gtts import gTTS
import os
from utils import *




toy = scanner.find_toy(toy_name="SB-69F1")
with SpheroEduAPI(toy) as droid:

    # go through the instructions
    speak("Hello, I am Sphero, and let's do a fun little challenge together. We'll see how long you can hold your breath! While you do it, please focus your attention on me. Are you ready?")
    time.sleep(2)
    speak("Great! Now we will begin. Please keep track of how long you've held your breath. If you can no longer hold your breath and I'm still talking, just ignore the rest of my instructions")
    time.sleep(2)
    speak("The game starts now. Take a long breath in")
    # start focus exercise
    # droid.scroll_matrix_text("Hello world", Color(r=0, g=0, b=255), 40, True)
    for _ in range(4):
         speak('let go of all your thoughts and focus on this present moment')
        #  for i in range(5):
         droid.scroll_matrix_text("calm calm calm", Color(r=0, g=0, b=255), 9, False)
         time.sleep(5)
            # time.sleep
         speak('if your mind is wandering, that is ok. Just gently pull it back into the presence')
         droid.scroll_matrix_text("calm calm calm calm calm calm", Color(r=0, g=0, b=255), 9, False)

         time.sleep(10)

