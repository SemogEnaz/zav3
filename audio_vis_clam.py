import sys

from file_io import IO

from vis_types.visualizer import Vis
from vis_types.bounce import Bounce
from vis_types.wave import Wave

class Clam():

    def __init__(self, default_resolution=20):

        # getting the command line arguments
        self.args = sys.argv[1:]
        self.num_args = len(self.args)

        """ 
        list of valid command line arguments
        r: read data for music file(s? :))
        c: create data and data_file form music files
        None: sets a default value to the dimensons
        """

        # All the stuff generated using the command line will be stored here and 
        # we will retrive it into main when needed
        self.resolution = default_resolution
        self.data = None
        self.vis = None

        self.audio_path = 'music/Let U Go-fXF59UWr-tA.wav'
        self.exe_cmd_args(self.args)

    def exe_cmd_args(self, args: list) -> None:

                                    # Usage of each argument
        self.get_audio_files(args)  #   -s "path/to/file"
        self.set_resolution(args)   #   -rez (int), only useable with 'c'
        self.make_data(args)        #   c or r, create form *.wav or read form data.txt
        self.make_frames(args)      #   bl or dl, bounce line or data line

        return

    def get_audio_files(self, args) -> None:

        if '-s' not in args:
            return
        
        index = args.index('-s') + 1

        file_name = args[index]

        # checking if the user wants to play only a single file & setting audio_path
        if '.wav' in file_name:
            self.audio_path = file_name
            return

        # manage multiple files

        pass

    def set_resolution(self, args):

        if 'r' in args:
            return
        
        resolution_arg = 'rez'

        if resolution_arg not in args:
            return

        index = args.index(resolution_arg)
        rez = args[index + 1]

        self.resolution = int(rez) 

    def make_data(self, args) -> None:

        io = IO(self.resolution)
        data = None

        if 'r' in args or len(args) == 0:
            data = io.read_audio_file()
            # Here the prior freq is saved in the last line of the audio_data file
            self.resolution = io.frequency 
        elif 'c' in args:
            data = io.make_audio_file(self.audio_path)

        self.data = data

        return

    def make_frames(self, args) -> None:

        vis = None

        if 'bl' in args:
            vis = Bounce(self.data)
            vis.make_bounce_frames()
        elif 'dl' in args:
            frames = self.data
        elif 'wl' in args or len(args) == 0:
            vis = Wave(self.data)
            vis.make_wave_frames()

        self.vis = vis

        return
