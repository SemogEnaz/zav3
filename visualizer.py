
class Vis():

    def __init__(self, audio_data: list[str]):

        # These are the number of digits of the data from each line we want.
        self.from_index = 2
        self.till_index = 6

        # Set the audio data so that we can make the frames later
        self.audio_data = audio_data
        self.max_value = self.get_max()

    def get_max(self) -> int:

        a = self.from_index
        b = self.till_index
        
        # Convert the string data into floats, doing this to get the max value
        int_list = [float(x[a:b]) for x in self.audio_data]
        max_value = max(int_list)

        return max_value

    def make_bounce_frames(self) -> list[str]:

        a = self.from_index
        b = self.till_index
        max_width = 90
        bounce_line_frames = []

        for data in self.audio_data:

            number = float(data[a:b])

            per_cent = number/self.max_value

            number = round(per_cent * max_width)

            line = '|' * number

            bounce_line_frames.append(line)

        return bounce_line_frames
        
