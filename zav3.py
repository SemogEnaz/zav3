from terminal_output import Screen
from audio_vis_clam import Clam

from vis_types.visualizer import Vis
from vis_types.bounce import Bounce
from vis_types.wave import Wave

import time
import subprocess
import threading

def main():

    clam = Clam()

    data = clam.data
    vis = clam.vis
    data_points = len(data)
    sleep_time = 1/clam.resolution

    audio_path = clam.audio_path

    auido_event = make_audio_event(audio_path)
    vis_event = make_vis_event(vis, sleep_time)

    run_events(auido_event, vis_event)

    return

def make_audio_event(audio_path: str):

    def music_command(audio_path, event) -> None:

        # We want the music to only start once the visualizer starts printing output
        event.wait() 

        # Starts music with mpv and does not output the regular terminal info
        subprocess.run(['mpv', '--no-video', '--no-terminal', audio_path], stderr=subprocess.DEVNULL)

    event = threading.Event() # This event represents starting the music

    # Creating and starting the thread
    audio_thread = threading.Thread(target=music_command, args=(audio_path, event,))
    audio_thread.start()

    return event

def make_vis_event(vis: Vis, sleep_time):
    """
    This function has some syncronization issues, if the precision is very high for the 
    data, the number of wait and print operations will cause an overall delay in the visualizer
    This can be overcome if we print in chunks instead of per line, eg 2 lines of the array are 
    printed per wait operation
    """

    def run_vis(vis: Vis, event, sleep_time) -> None:

        event.wait()

        vis.print_frames(sleep_time)

        return

    event = threading.Event() # This event represents starting the music

    # Creating and starting the thread
    vis_thread = threading.Thread(target=run_vis, args=(vis, event, sleep_time))
    vis_thread.start()

    return event

def run_events(audio_event, vis_event) -> None:

    audio_event.set()
    vis_event.set()

    return

main()
