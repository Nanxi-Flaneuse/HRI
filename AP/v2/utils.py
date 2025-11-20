import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from gtts import gTTS
import os
import numpy as np
import asyncio
import functools

def speak(text):
    text_to_speak = text
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save("speech.mp3")
    os.system("afplay speech.mp3")

def get_random_color():
    return Color(r = np.random.randint(255), g = np.random.randint(255), b=np.random.randint(255))

async def wait_for_shakes(droid: SpheroEduAPI, goal_shakes: int, timeout: float | None = None):
    """
    Wait until `goal_shakes` collision events are received for `droid`.
    Uses SpheroEduAPI.register_event to receive collision events and an asyncio.Queue
    to count them in the event loop safely.

    Returns the number of shakes actually counted (goal_shakes if successful, else < goal_shakes on timeout).
    """
    loop = asyncio.get_running_loop()
    q: asyncio.Queue = asyncio.Queue()
    count = 0

    # Thread-safe callback invoked by spherov2; it runs outside asyncio loop in a thread.
    def _on_collision(loop_ref, queue_ref, _event_packet):
        # just push a simple marker into the queue
        loop_ref.call_soon_threadsafe(queue_ref.put_nowait, True)

    # Register event using classmethod pattern from example
    SpheroEduAPI.register_event(droid, EventType.on_collision, functools.partial(_on_collision, loop, q))

    try:
        while count < goal_shakes:
            try:
                # wait for next collision marker (with optional timeout)
                await asyncio.wait_for(q.get(), timeout=timeout)
                count += 1
                # feedback for each registered shake
                try:
                    droid.set_main_led(get_random_color())
                except Exception:
                    # non-fatal: continue even if LED fails
                    pass
                os.system("afplay /System/Library/Sounds/Glass.aiff")

                # Sound.Effects.BeepSingle.play(False)
            except asyncio.TimeoutError:
                break
    finally:
        # Put unregister event method here if possible
        pass

    return count