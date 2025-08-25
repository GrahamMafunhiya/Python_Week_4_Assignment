# Open the file for reading

with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content 
modified_content = content.upper()

# Open a new file for writing and save the modified content
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified version written to output.txt")