import math

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

    def get_relevant_data(self):

        a = self.from_index
        b = self.till_index

        fixed_data = [float(data[a:b]) for data in self.audio_data]

        return fixed_data

if __name__ == '__main__':
    pass
