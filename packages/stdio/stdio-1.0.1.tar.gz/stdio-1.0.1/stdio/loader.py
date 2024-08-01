import math
import shutil
import sys
from typing import Optional, Union
from stdio import write, deleteline, skipline


class Loader:
    def __init__(self,
                 min_progress: int = 0,
                 max_progress: int = 100,
                 current_progress: Optional[int] = None,
                 scale: float = 1,
                 pre_string: str = "progress_total_number",
                 fill_string: str = "█",
                 empty_string: str = " ",
                 border_string: str = "│"
                 ):
        self.min_progress = min_progress
        self.max_progress = max_progress
        self.current_progress = min_progress if current_progress is None else current_progress
        self.scale = scale

        self.pre_string = pre_string
        self.fill_string = fill_string
        self.empty_string = empty_string
        self.border_string = border_string
        self.state = "loading"

        skipline()
        self.render()

    def progress(self, current_progress):
        self.state = "progress"
        self.current_progress = current_progress

        self.render()

    def increase(self, increment):
        self.state = "progress"
        self.current_progress += increment

        self.render()
    
    def complete(self):
        self.current_progress = self.max_progress
        self.state = "success"

        self.render()

    def error(self):
        self.state = "error"

        self.render()
 
    def end(self):
        skipline(2)

    def erase(self):
        deleteline(math.ceil(self.scale))
        skipline()

    def render(self):
        if self.current_progress < self.min_progress:
            self.current_progress = self.min_progress
        elif self.current_progress > self.max_progress:
            self.current_progress = self.max_progress

        if self.pre_string == "progress_number":
            pre_string = f"{self.current_progress}/{self.max_progress} {self.border_string}"
        elif self.pre_string == "progress_total_number":
            pre_string = f"{self.current_progress}/{self.max_progress} {self.border_string}"
        else:
            pre_string = f"{self.pre_string}{self.border_string}"

        terminal_size = shutil.get_terminal_size().columns

        aditional_length = len(pre_string + self.border_string) * (math.floor(self.scale) - 1)
        
        loader_length = math.floor((terminal_size - len(pre_string + self.border_string)) * self.scale) + aditional_length

        progress_length_ = math.floor(((self.current_progress - self.min_progress) * loader_length) / (self.max_progress - self.min_progress))


        self.erase()

        write(pre_string)

        if self.state == "progress":
            sys.stdout.write('\x1b[33m')  # Amarelo
        elif self.state == "success":
            sys.stdout.write('\x1b[32m')  # Verde
        elif self.state == "error":
            sys.stdout.write('\x1b[31m')  # Vermelho

        for i in range(loader_length):
            if i < progress_length_:
                write(self.fill_string)
            else:
                write(self.empty_string)

        sys.stdout.write('\x1b[0m')

        write(self.border_string)
        sys.stdout.flush()
