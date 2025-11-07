import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from gtts import gTTS
import os
from utils import *




toy = scanner.find_toy(toy_name="SB-69F1")
with SpheroEduAPI(toy) as droid:
    # speak('hello world. This is Sphero')
    droid.set_main_led(Color(r=0, g=0, b=255))
    
    droid.set_speed(60)
    time.sleep(2)
    droid.set_speed(0)

    for _ in range(4):
        droid.roll((droid.get_heading() + 90), 60, 1)
        # droid.delay(0.5)
    speak("Hello World")
    droid.scroll_matrix_text("Hello world", {'r': 150, 'g': 50, 'b': 0}, 40, True)
    droid.set_main_led({'r': 0, 'g': 0, 'b': 255})

    droid.set_main_led(get_random_color())
    # droid.Sound.Personality.Dreaming.play()
    droid.roll((droid.get_heading() + 90), 20, 1)
    time.sleep(0.2)

    # # self intro with scroll_matrix_text
    speak('Hello! My name is Sphero, and I love mindful practices like meditation and yoga!')
    time.sleep(0.3)
    # droid.Sound.Personality.Yipee.play()
    droid.roll((droid.get_heading() + 30), 50, 0.5)
    speak("What kind of mindful activities do you enjoy? There\'s one meditation I love in particular, it is the breathing meditation. Here\'s how I do it!")
    for _ in range(2):
            droid.set_main_led(get_random_color())
            droid.roll((droid.get_heading() + 180), 40, 2)
            speak("Breathe in")
            droid.roll((droid.get_heading() + 180), 40, 2)
            speak("Breathe out")

    droid.roll(180, 50, 0.2)
    time.sleep(1)
    speak('I also like going to the beach in my free time and hear the sound of the waves and feel the softness of the sand as I roll across the beach.')
    droid.roll(210, 70, 2)
    speak("I sometimes imagine myself turning into a sea urchin and resting among the corals. What fun!")
    droid.set_main_led({'r': 72, 'g': 255, 'b': 245})
    droid.roll(180, 45, 1)
    
    speak('That\'s the end of my introduction. I hope we can learn more about each other. Bye!')
    time.sleep(1)
    droid.scroll_matrix_text('bye bye', {'r': 255, 'g': 162, 'b': 48}, 13, False)