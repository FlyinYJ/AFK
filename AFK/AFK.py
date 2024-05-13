import random
import time

import pyautogui as pg
from alive_progress import alive_bar


def AFK(duration=1, verbose=None):
    """Main function to move the mouse for duration in minutes

    Args:
        duration (int, optional): Total length of jiggering. Defaults to 1 min.
        verbose (_type_, optional): debug mode. Defaults to None.
    """
    duration = int(duration)  # * 60
    with alive_bar(duration) as bar:
        while duration > 0:
            # print(f"time left: {duration}s")
            move_x = random.sample(range(-3, 3), 1)[0]
            sleep_duration = random.sample(range(1, 10), 1)[0]
            if sleep_duration > duration:
                sleep_duration = duration

            time.sleep(sleep_duration)

            if verbose:
                print(f"moving {move_x}px")
            pg.moveRel(move_x, move_x)

            progress = sleep_duration
            duration -= progress
            bar(progress)
