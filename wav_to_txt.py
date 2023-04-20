from terminal_output import Screen
from audio_vis_clam import Clam

import time
import subprocess
import threading

def main():

    clam = Clam()

    audio_path = './Let U Go-fXF59UWr-tA.wav'

    auido_event = make_audio_event(audio_path)
    vis_event = make_vis_event(clam.data)
    
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

def make_vis_event(audio_data: list[float]):

    def run_vis(audio_data: list[float], event) -> None:

        event.wait()

        for data in audio_data:
            return_car_line(data)
            time.sleep(0.0625)
        return

    event = threading.Event() # This event represents starting the music

    # Creating and starting the thread
    vis_thread = threading.Thread(target=run_vis, args=(audio_data, event,))
    vis_thread.start()

    return event

def return_car_line(text: float) -> None:
    print(text + '\r', end="")

def run_events(audio_event, vis_event) -> None:

    audio_event.set()
    vis_event.set()

    return


main()
