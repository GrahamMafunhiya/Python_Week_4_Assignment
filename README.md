# Python_Week_4_Assignment
Assignment for Python Week 4

# Python File Handling Programs

This repository contains two simple Python programs that demonstrate
file handling: reading, writing, and error handling.

------------------------------------------------------------------------

## Program 1: Basic File Read and Write

**File:** `basic_file_rw.py`

### Description

-   Reads content from `input.txt`
-   Converts the text to uppercase (as an example modification)
-   Writes the modified content into `output.txt`

### Example Code

``` python
with open("input.txt", "r") as infile:
    content = infile.read()

modified_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)
```

------------------------------------------------------------------------

## Program 2: User Input with Error Handling

**File:** `file_rw_with_errors.py`

### Description

-   Asks the user to provide a filename
-   Reads the file if it exists
-   Reverses the content (as an example modification)
-   Saves the modified content to a new file named `modified_<filename>`
-   Handles errors such as:
    -   File not found
    -   Permission denied
    -   Other unexpected errors

### Example Code

``` python
try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as infile:
        content = infile.read()

    modified_content = content[::-1]
    new_filename = "modified_" + filename

    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"Modified file saved as {new_filename}")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

------------------------------------------------------------------------

## How to Run

1.  Save the code snippets into `.py` files (`Error Handling.py` and
    `File Read and Write.py`).

2.  Run them using:

    ``` bash
    Error Handling.py
    File Read and Write.py
    ```

3.  Ensure you have a text file (`input.txt` or a filename you provide)
    in the same directory.

------------------------------------------------------------------------

## Notes

-   You can change the modification logic (uppercase, reverse, replace
    words, etc.) to fit your needs.
-   Always use the `with open(...)` syntax to ensure files are properly
    closed.
