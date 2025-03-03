from pathlib import Path

from .startup import *  # Imports the pre-processed command-line arguments
from .program import Program

class Filter(Program):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_files(self):
        for file in ARGS.args:
            if not os.path.exists(file):
                print(f"File does not exist: {file}")
                continue

            if os.path.isdir(file):
                if RECURSIVE:
                    for root, _, files in os.walk(file, followlinks=FOLLOW):
                        for f in files:
                            print(os.path.join(root, f))
                else:
                    self.process(file)
            else:
                self.process(file)

    def process(self, s):
        print(s)

if __name__ == "__main__":
    filter_program = Filter()
    filter_program.process_files()
