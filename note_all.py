import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
import os
import asyncio
import threading
import numpy as np
import struct
import sys

#colors
red=Color(r=255, g=0, b=0)
green=Color(r=0, g=255, b=0)
blue=Color(r=0, g=0, b=255)
off=Color(0,0,0)
white=Color(255,255,255)
yellow=Color(255,255,0)
orange=Color(255,165,0)

 

toy = scanner.find_toy(toy_name="SB-FA10")
with SpheroEduAPI(toy) as api:
    #####Conditional
    # while True:
        # gyro = api.get_gyroscope() or {}  
        # velo = api.get_velocity() or {} #overlapp with gyroscope, not sure how to distinguish
            
        # if abs(gyro.get('y', 0)) > 75:
        #         os.system('say "Dizzy. Dizzy"')
               
        # if api.get_luminosity_direct() < 50:
        #         os.system('say "Too dark here"')
              


    
    #####Show real time data for gyroscope (include x, y, z) & luminocity
    # while True:
    #     gyro = api.get_gyroscope()
    #     lumi = api.get_luminosity_direct()
    #     print(gyro)
    #     print(lumi)
    #     time.sleep(0.3)






    # #####Show something on matrix or Create animation
    # arrow = np.rot90(np.array([
    #     [0,0,0,4,4,0,0,0],
    #     [0,0,4,4,4,4,0,0],
    #     [0,4,4,4,4,4,4,0],
    #     [0,0,0,4,4,0,0,0],
    #     [0,0,0,4,4,0,0,0],
    #     [0,0,0,4,4,0,0,0],
    #     [0,0,0,4,4,0,0,0],
    #     [0,0,0,4,4,0,0,0]]), k=2)
    # flash = np.rot90(np.array([
    #     [0,0,5,0,0,0,0,0],
    #     [0,0,0,5,0,0,0,0],
    #     [0,0,0,5,5,0,0,0],
    #     [0,0,0,0,5,5,0,0],
    #     [0,5,5,5,5,5,5,0],
    #     [0,0,5,5,0,0,0,0],
    #     [0,0,0,5,0,0,0,0],
    #     [0,0,0,0,5,0,0,0]]), k=2)
    # blank = np.rot90(np.array([
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0]]), k=2)

    # def matrix_arrow(api):
    #     api.register_matrix_animation(
    #         frames=[arrow],
    #         palette=[off,yellow,red,green,orange,blue], #color index for creating frames above
    #         fps=5, #small number is slower
    #         transition=False)
    #     api.play_matrix_animation(0, False)
    #     time.sleep(1)
    #     api.clear_matrix()
   
    # def matrix_flash(api):
    #     api.register_matrix_animation(
    #         frames=[flash],
    #         palette=[off,yellow,red,green,orange,blue],
    #         fps=5, #small number is slower
    #         transition=False)
    #     api.play_matrix_animation(0, False)
    #     time.sleep(1)
    #     api.clear_matrix()

    # def matrix_blank(api):
    #     api.register_matrix_animation(
    #         frames=[blank],
    #         palette=[off,yellow,red,green,orange,blue], #color index for creating frames above
    #         fps=5, #small number is slower
    #         transition=False)
    #     api.play_matrix_animation(0, False)
    #     time.sleep(1)
    #     api.clear_matrix()
    
    # def animation (api):
    #     api.register_matrix_animation(
    #         frames=[arrow, blank, flash, blank, arrow, blank, flash, blank],
    #         palette=[off,yellow,red,green,orange,blue], #color index for creating frames above
    #         fps=3, #small number is slower
    #         transition=False)
    #     api.play_matrix_animation(0, False)
    #     time.sleep(5) #animation takes slightly longer, so see everything
    #     api.clear_matrix()
    

    # ###show single flame on matrix
    # matrix_arrow(api)
    # matrix_flash(api)
    # matrix_blank(api)

    # ###show animation
    # animation(api)