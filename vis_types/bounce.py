import time
from visualizer import Vis

class Bounce(Vis):

    def make_frames(self) -> None:

        max_width = 90
        bounce_line_frames = []

        audio_data = self.get_relevant_data()

        for data in audio_data:

            per_cent = data/self.max_value

            index = round(per_cent * max_width)

            line = '|' * index

            bounce_line_frames.append(line)

        self.frames = bounce_line_frames

    def print_frames(self, wait_time) -> None:

        for row in self.frames:
            print(row)
            self.sleep(wait_time) 
