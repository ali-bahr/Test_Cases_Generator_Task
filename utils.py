import re
import csv

def read_input_file(file_path: str) -> list[str]:
    """
    Read options from a file and return them as a list.
    Each option should be written in separate line.
    """
    try:
        with open(file_path, 'r') as file:
            options = []
            for line in file:
                if line.strip():
                    options.append(line.strip())
            return options
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")


def has_special_character(s: str) -> bool:
    """
    Check if the string contains any special characters.
    """
    return bool(re.search(r'[^a-zA-Z0-9]', s))


def validate_inputs(options: list) -> None:
    if len(options) == 0:
        raise ValueError("Empty options is invalid.")

    if len(set(options)) != len(options):
        raise ValueError("Repeated options name is invalid.")

    for option in options:
        if has_special_character(option):
            raise ValueError(f"Option '{option}' contains special characters, which is invalid.")


def write_output_file(test_cases: list[dict], output_file) -> None:
    try:
        with open(output_file, 'w') as csvfile:
            headers = list(test_cases[0].keys())
            headers = ["Test Case ID"] + headers
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for i, test_case in enumerate(test_cases):
                test_case["Test Case ID"] = i+1
                writer.writerow(test_case)
    except Exception as e:
        raise Exception(f"An error occurred while writing to the file: {e}")