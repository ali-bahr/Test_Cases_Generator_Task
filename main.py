import itertools
import sys
from utils import read_input_file, validate_inputs, write_output_file


def run_test_case(test_case: dict, options) -> None:
    """
    Simulate running a test case.
    This function would contain the logic to execute the test case.
    """

    valid_tc = True
    for option in options:
        if not valid_tc:
            break

        if test_case[f"Slave Option Of {option}"] == "NA":
            continue

        if test_case[f"Master Option Of {option}"] == "NA":
            valid_tc = test_case[f"Slave Option Of {option}"] != "False"
            continue

        if test_case["Master Option Of " + option] != test_case["Slave Option Of " + option]:
            valid_tc = False

    # Initialize expected values for each option
    test_case["ValidTC"] = "False"
    for option in options:
        test_case["Expected Of " + option] = "NA"

    if valid_tc:
        test_case["ValidTC"] = "True"
        for option in options:
            if test_case["Master Option Of " + option] == "NA":
                test_case["Expected Of " + option] = "True"
                continue
            test_case["Expected Of " + option] = test_case["Master Option Of " + option]


def generate_test_cases(options: list[str]) -> list:

    possible_values = ["True", "False", "NA"]
    master_options = ["Master Option Of " + option for option in options]
    slave_options = ["Slave Option Of " + option for option in options]
    combined_options = master_options + slave_options

    combinations = list(itertools.product(possible_values, repeat=len(combined_options)))
    combinations = [dict(zip(combined_options, combination)) for combination in combinations]
    print (combinations)
    for combination in combinations:
        for option in options:
            run_test_case(combination, options)

    return combinations


def main(options: list, output_file = "./output.csv") -> None:
    try:
        validate_inputs(options)
        print("Options are valid.")
        test_cases = generate_test_cases(options)

        write_output_file(test_cases, output_file)

    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)




if __name__ == '__main__':
    options = []
    # Here I will check if options are provided as command line arguments
    # or I need to read from an input file
    if len(sys.argv) > 1:
        options = sys.argv[1:]
    else:
        options = read_input_file("input.txt")

    main(options)
