import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from gtts import gTTS
import os
import numpy as np
import asyncio

num_shakes = 0

def speak(text):
    text_to_speak = text
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save("speech.mp3")
    os.system("afplay speech.mp3")

def get_random_color():
    return Color(r = np.random.randint(255), g = np.random.randint(255), b=np.random.randint(255))


""" Increment the num_shakes counter by 1 every time a collision shake event is registered. 

"""
async def when_collision_shake(droid, goal_shakes):

    global num_shakes
    start_count = num_shakes
    
    while num_shakes - start_count < goal_shakes:
        events = droid.get_pending_events()
        for evt in events:

            if hasattr(evt, "event_type") and evt.event_type.name == "COLLISION":
                num_shakes += 1
                Sound.Effects.BeepSingle.play(False)
                droid.set_main_led(get_random_color())
        time.sleep(0.1)  # poll interval to check shake progress

