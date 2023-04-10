import time
from visualizer import Vis
import shutil

class Wave(Vis):

    def __init__(self, audio_data, max_height=20):
        super().__init__(audio_data)
        self.max_height = max_height
        self.col_count = 0
        self.char = '|'
        self.is_hollow = False

    def make_frames(self) -> None:
        audio_data = self.get_relevant_data()

        max_height = self.max_height

        wave_array = [[' ' for _ in range(len(audio_data))] for _ in range(max_height)]

        for col_count, data in enumerate(audio_data):
            per_cent = data/self.max_value
            index = round(per_cent * max_height)
            wave_array = self.fill_col(index, col_count, wave_array)

        self.frames = wave_array

    def fill_col(self, index: int, col_count: int, array):

        height = len(array)

        for row_count in range(height):

            if row_count > index:
                break

            row_index = height - row_count - 1
            
            if self.is_hollow:
                if row_count < index:
                    array[row_index][col_count] = ' '
                else:
                    array[row_index][col_count] = self.char
            else:
                array[row_index][col_count] = self.char
                
        return array

    def print_frames(self, wait_time) -> None:
        # TODO: remove the array we use to render, directly index the frames made by the 
        # make frames function above, this should lead to faster render speed

        height = self.max_height
        width = self.get_width() // 2
        array = ["" for _ in range(height)] # This is the array we will use to render

        for _ in self.frames[0]:

            # Removing last col form array and appending new col to back
            for row_index, row in enumerate(array):
                if len(row) == width:
                    row = row[1:] + self.frames[row_index][self.col_count]
                else:
                    row += self.frames[row_index][self.col_count]

                array[row_index] = row

            # Print a regularly
            for row in array:
                print(row)

            # Print the reverse rows for the bottom part of the wave
            for row in array[::-1]:
                print(row)


            self.col_count += 1

            self.move_cursor_up(2*self.max_height)
            print('\r', end='')

            # For some reason the speed lines up better for rez 8 to 20 when we reduce the
            # calculated wait time by 5%
            # TODO: Look into this later...
            self.sleep(wait_time - (0.05 * wait_time))

    def get_width(self):
        # get terminal width
        term_size = shutil.get_terminal_size()
        return term_size.columns

    def move_cursor_up(self, num_lines=1):
        # \33[F is the code to move the cursor up
        print('\33[F' * num_lines, end='')
