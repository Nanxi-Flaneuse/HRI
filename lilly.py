async def start_program():
    # Blocks to use in Step 1
    # set_stabilization(False)
    # human speak: Hi Sphero, I will take you to see a new friend today! Are you excited?
    await delay(6)
    await speak("Oh my god, yes! ")
    await delay(0.2)
    await Sound.Personality.Yipee.play()
    await delay(0.2)
    await speak("What is their name?")
    # make funny sound and wiggle
    await spin(45, 0.2)
    await spin(-45, 0.2)
    await spin(45, 0.2)
    await spin(-45, 0.2)
    await spin(45, 0.2)
    await spin(-45, 0.2)
    await spin(45, 0.2)
    await spin(-45, 0.2)

    # human speak: You will know when you get there

    # huamn speak: We are here. Meet your new friend Lilly the sea otter! She is from the kelp forest in Monterey bay!
    await delay(8)
    # sphero displays smile
    play_matrix_animation(0, True)

    # play_matrix_animation(0, True)
    await speak("Nice to meet you Lilly! I'm Sphero. Since I don't have hands, is it ok if I give you a hug?")
    await clear_matrix()

    # human speak: yes, it is ok
    await delay(2)
    # Sphero approaches Lilly and lightly touches her as a way of saying Hello, then takes a few steps back
    
    await roll(0, 80, 3)
    # if get_location() == get_location():
    #     await speak("Oh la la your fur is soft!")
    await delay(1)
    await roll(180, 90, 2)
    await delay(5)
    await spin(180,0.5)
    # human speak: do you want to know what she has in her hand? Points to Lilly
    await delay(8)
    await speak("what is it you're holding in your hand Lilly?")
    await delay(0.2)
    await Sound.Personality.Curious.play()
    await delay(10)
    # # human speak: it's a starfish! As a keystone species in the Monterey bay, sea otters eat a lot of food everyday and starfish is definitely on their menu!

    await speak("I see! That is so interesting! I've never had a starfish before but I can draw one! Here it is")

    # Sphero displays starfish
    play_matrix_animation(1, True)
    
    await delay(5)
    await clear_matrix()
    # # human speak: Nice drawing! 
    await delay(5)
    await speak("thank you!")
    # human speak: Well i think it's time for Lilly to take a nap, would you like to say bye to her?
    await delay(8)
    await speak("Ok! Bye Lilly! I'll see you next time!")
    # # sphero wiggles its body to say goodbye
    await spin(45, 0.3)
    await spin(-45, 0.3)
    await spin(45, 0.3)
    await spin(-45, 0.3)


register_matrix_animation({'frames': [[[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 4, 4, 1, 1, 4, 4, 1],
        [1, 4, 4, 1, 1, 4, 4, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 4, 1, 1, 1, 1, 4, 1],
        [1, 1, 4, 1, 1, 4, 1, 1],
        [1, 1, 1, 4, 4, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]],
    [[1, 4, 4, 1, 1, 4, 4, 1],
        [4, 1, 1, 4, 4, 1, 1, 4],
        [4, 1, 1, 4, 4, 1, 1, 4],
        [1, 4, 4, 1, 1, 4, 4, 1],
        [1, 4, 1, 1, 1, 1, 4, 1],
        [1, 1, 4, 1, 1, 4, 1, 1],
        [1, 1, 4, 4, 4, 4, 1, 1],
        [1, 1, 1, 4, 4, 1, 1, 1]]], 'palette': [{'r': 255, 'g': 255, 'b': 255},
    {'r': 0, 'g': 0, 'b': 0},
    {'r': 255, 'g': 0, 'b': 0},
    {'r': 255, 'g': 64, 'b': 0},
    {'r': 255, 'g': 128, 'b': 0},
    {'r': 255, 'g': 191, 'b': 0},
    {'r': 255, 'g': 255, 'b': 0},
    {'r': 185, 'g': 246, 'b': 30},
    {'r': 0, 'g': 255, 'b': 0},
    {'r': 185, 'g': 255, 'b': 255},
    {'r': 0, 'g': 255, 'b': 255},
    {'r': 0, 'g': 0, 'b': 255},
    {'r': 145, 'g': 0, 'b': 211},
    {'r': 157, 'g': 48, 'b': 118},
    {'r': 255, 'g': 0, 'b': 255},
    {'r': 204, 'g': 27, 'b': 126}], 'fps': 10, 'transition': MatrixAnimationTransition.NONE})


# async def start_program():
#     await Sound.EightBit.Blip.play(True)
#     await roll(134, 115, 5)
#     play_matrix_animation(0, True)
# async def on_collision():
#     await speak('ouch', False)
# register_event(EventType.ON_COLLISION, on_collision)
register_matrix_animation({'frames': [[[1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 2, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]],
    [[1, 1, 5, 5, 1, 1, 1, 1],
        [1, 1, 5, 5, 5, 1, 1, 1],
        [1, 1, 5, 1, 1, 5, 5, 5],
        [5, 5, 5, 1, 1, 1, 1, 5],
        [5, 1, 1, 1, 1, 1, 5, 1],
        [1, 5, 1, 1, 5, 1, 5, 1],
        [1, 1, 5, 5, 1, 5, 5, 1],
        [1, 1, 5, 1, 1, 1, 5, 1]]], 'palette': [{'r': 255, 'g': 255, 'b': 255},
    {'r': 0, 'g': 0, 'b': 0},
    {'r': 255, 'g': 0, 'b': 0},
    {'r': 255, 'g': 64, 'b': 0},
    {'r': 255, 'g': 128, 'b': 0},
    {'r': 255, 'g': 191, 'b': 0},
    {'r': 255, 'g': 255, 'b': 0},
    {'r': 185, 'g': 246, 'b': 30},
    {'r': 0, 'g': 255, 'b': 0},
    {'r': 185, 'g': 255, 'b': 255},
    {'r': 0, 'g': 255, 'b': 255},
    {'r': 0, 'g': 0, 'b': 255},
    {'r': 145, 'g': 0, 'b': 211},
    {'r': 157, 'g': 48, 'b': 118},
    {'r': 255, 'g': 0, 'b': 255},
    {'r': 204, 'g': 27, 'b': 126}], 'fps': 10, 'transition': MatrixAnimationTransition.NONE})

async def on_collision():
    await Sound.EightBit.Blip.play(True)
    await speak("Ouch! Why did you stop me?")
    # await roll(134, 115, 5)
    # # play_matrix_animation(0, True)
    # await speak("Wow your fur is so soft!")
register_event(EventType.ON_COLLISION, on_collision)