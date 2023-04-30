import librosa
import numpy as np

class IO():

    def __init__(self, frames_per_second: int):
        self.frequency = frames_per_second
        self.output_file = './audio_data.txt'

    def read_audio_file(self) -> list[str]:
        data = []

        with open(self.output_file, 'r') as file:
            for line in file:
                line = self.sci_to_float(line)
                data.append(line)

        self.frequency = int(float(data[-1]))
        data = data[:-1]

        return data
    
    def sci_to_float(self, text: str) -> str:

        exponent = len(text)
        format_string = '{:.' + str(exponent) + 'f}'
        num = format_string.format(float(text))
        num = str(num)

        return num
    
    def make_audio_file(self, audio_path='') -> list[str]:

        # Load the audio file
        audio_data, sr = librosa.load(audio_path, sr=44100)  # 44100 44.1kHz sampling rate

        # Divide the audio data into 1ms intervals
        ms = int(sr/self.frequency)  # number of samples per millisecond
        audio_data_ms = [audio_data[i:i+ms] for i in range(0, len(audio_data), ms)]

        # Calculate the value of the audio signal at each time interval
        audio_data_ms_avg = np.array([np.mean(np.abs(x)) for x in audio_data_ms])

        # Saving the frequency to the end of the file
        frequency_data = self.frequency
        frequency_data = np.array([frequency_data], dtype=object)
        audio_data_ms_avg = np.append(audio_data_ms_avg, frequency_data)

        np.savetxt(self.output_file, audio_data_ms_avg) # Can be used for diagonstics

        audio_data_ms_avg = audio_data_ms_avg[:-1]

        return [str(data_line) for data_line in audio_data_ms_avg]
