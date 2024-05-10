import random

import pyautogui as pg
from alive_progress import alive_bar


def AFK(duration=1, verbose=None):
    """Main function to move the mouse for duration in minutes

    Args:
        duration (int, optional): Total length of jiggering. Defaults to 1 min.
        verbose (_type_, optional): debug mode. Defaults to None.
    """
    duration = int(duration) * 60
    with alive_bar(duration) as bar:
        while duration > 0:
            # print(f"time left: {duration}s")
            random_combo = random.sample(range(1, 10), 2)
            move_x = random_combo[0]
            if random_combo[1] <= duration:
                move_duration = random_combo[1]
            else:
                move_duration = duration

            if verbose:
                print(f"moving {move_x}px in {move_duration}s")
            pg.moveRel(move_x, 0, duration=move_duration)

            if duration < move_duration:
                progress = duration
            else:
                progress = move_duration
            duration -= progress
            bar(progress)
