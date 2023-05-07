
class Screen():

    def text_to(self, color_code, string):
        return color_code + string + '\033[0m'

    def text_to_green(self, string):
        return text_to('\033[32m', string)

    
    def move_cursor_down(self, num_lines=1):
        print('\33[E' * num_lines, end='')


    def move_cursor_up(self, num_lines=1):
        print('\33[F' * num_lines, end='')
