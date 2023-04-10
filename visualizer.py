import math
import time
from abc import ABC, abstractmethod

class Vis(ABC):

    def __init__(self, audio_data) -> None:

        # These are the number of digits of the data from each line we want.
        self.from_index = 2
        self.till_index = 8

        # Set the audio data so that we can make the frames later
        self.audio_data = audio_data
        self.max_value = self.get_max()
        self.frames = None

    def get_max(self) -> int:

        a = self.from_index
        b = self.till_index
        
        # Convert the string data into floats, doing this to get the max value
        int_list = [float(x[a:b]) for x in self.audio_data]
        max_value = max(int_list)

        return max_value

    def get_relevant_data(self) -> float:

        a = self.from_index
        b = self.till_index

        fixed_data = [float(data[a:b]) for data in self.audio_data]

        return fixed_data

    def sleep(self, wait_time) -> None:
        time.sleep(wait_time)

    @abstractmethod
    def make_frames(self) -> None:
        """
        This method will be what generates the frames for the visualizer, each vis
        will implement this obv.
        """
        pass

    @abstractmethod
    def print_frames(self, wait_time) -> None:
        """
        This is a pretty important method, it is used to display a frame of data
        corresponding to every tick on auido/time
        """
        pass

if __name__ == '__main__':
    pass
