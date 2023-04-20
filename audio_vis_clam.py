import sys
import librosa
import numpy as np

class Clam():

    def __init__(self):

        # getting the command line arguments
        self.args = sys.argv[1:]
        self.num_args = len(self.args)

        """ 
        list of valid command line arguments
        r: read data for music file(s? :))
        c: create data and data_file form music files
        None: sets a default value to the dimensons
        """

        self.data = None

        self.exe_cmd_args()
        
    def exe_cmd_args(self) -> None:

        if 'r' in self.args or len(self.args) == 0:
            self.read_audio_file()
        elif 'c' in self.args:
            self.make_audio_file('./Let U Go-fXF59UWr-tA.wav')

    def read_audio_file(self) -> list[str]:
        data = []

        with open('./audio_data.txt', 'r') as file:
            for line in file:
                line = self.sci_to_float(line)
                data.append(line)

        self.data = data
    
    def sci_to_float(self, text: str) -> str:

        exponent = len(text)
        format_string = '{:.' + str(exponent) + 'f}'
        num = format_string.format(float(text))
        num = str(num)

        return num
    
    def make_audio_file(self, audio_path='') -> list[str]:

        # Load the audio file
        audio_data, sr = librosa.load(audio_path, sr=44100)  # 44.1kHz sampling rate

        # Divide the audio data into 1ms intervals
        ms = int(sr/16)  # number of samples per millisecond
        audio_data_ms = [audio_data[i:i+ms] for i in range(0, len(audio_data), ms)]

        # Calculate the value of the audio signal at each time interval
        audio_data_ms_avg = np.array([np.mean(np.abs(x)) for x in audio_data_ms])

        # Store the audio data in a text file
        output_file = './audio_data.txt'
        np.savetxt(output_file, audio_data_ms_avg) # Can be used for diagonstics

        self.data = [str(data_line) for data_line in audio_data_ms_avg]
