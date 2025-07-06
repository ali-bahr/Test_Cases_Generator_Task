import os
from main import main
from utils import read_input_file


def run_tests():
    """
    Run the main program against custom already made testcases.

    Testcases are located in ./tests/inputs directory and output files
    are stored in the ./tests/output directory.
    """

    input_files = os.listdir("./test/inputs")

    for input_file in input_files:
        options = read_input_file(f"./test/inputs/{input_file}")
        main(options, output_file=f"./test/outputs/{input_file.replace('.txt', '.csv')}")

run_tests()