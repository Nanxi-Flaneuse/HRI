import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
# from spherov
from gtts import gTTS
import os
from utils import *
from enum import Enum, IntEnum, auto

def state1_spin(droid):
    for _ in range(13):
        droid.roll(30, 0, 0.1)

def state2_scared():
    speak("I'm scared!")

def state3_happy(droid):
    pass

def state4_injured(droid):
    speak('Ouch! That hurts!')

def state5_terminal(droid):
    droid.scroll_matrix_text("Bye bye", {'r': 150, 'g': 50, 'b': 0}, 40, True)

def on_gyro_max(droid):
    droid.set_main_led({'r': 0, 'g': 0, 'b': 255})

def on_freefall():
    speak('ouch!')
    droid.set_main_led({'r': 0, 'g': 0, 'b': 255})
# toy = scanner.find_toy(toy_name="SB-BBBE")
# SpheroEduAPI.register_event(EventType.on_freefall, on_freefall)
toy = scanner.find_toy(toy_name="SB-69F1")
with SpheroEduAPI(toy) as droid:
    # droid.register_event(EventType.on_gyro_max, on_gyro_max)
    droid.register_event(EventType.on_freefall, on_freefall)
    speak('hello world. This is Sphero')
    # cross the road
    # droid.roll(0, 55, 2)
    # droid.roll(90, 55, 8)
    # # droid.roll(0, 60, 8)
    # droid.roll(-90, 60, 2)
    
