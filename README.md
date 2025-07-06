# Task 2
# Test Case Generation Script


## Requirements
- Python 3.8+

## Installation
No installation is needed for external libraries. 
Just Ensure you have Python installed.


## Running the Script
#### We can run the script and pass the server_options(input) using two options: 
1. **Using the command line**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the command:
     ```bash
     python main.py option1 option2 option3
     ```
>
> - the options should be passed separated by spaces. 
> - if there is no options are passed the script will continue and uses the second option to read the input.

2.**Reading `input.txt` file**:
    - Created a file named `input.txt` in the same directory as the script.
    - Write your server options in the file, each option on a new line.
    - Run the script using the command:
      ```bash
      python main.py
      ```

## Output
- If input is valid a CSV file `output.csv` will be made in the same directory.

## To Run all the possible tests:
   - you can run the script `test_all.py` which uses the files in the dir `.\test\inputs` and writes the outptus to `.\test\outputs`.
    ```     
    python test_all.py 
    ``` 