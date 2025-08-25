# Program to read a file from user input and write a modified version to a new file

try:
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    # Try to open the file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify the content (example: reverse the text)
    modified_content = content[::-1]

    # Create a new filename for the modified file
    new_filename = "modified_" + filename

    # Write the modified content to the new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"Modified file saved as {new_filename}")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")