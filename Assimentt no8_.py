Practical No: 8

Lab Assignment-1

Perform the following File Handling Operations.

a) Construct a program that reads a text file and writes its contents into a new text file with the same content, but in uppercase

# Program to convert file content to uppercase

# Input file name
source_file = input("Enter the source file name: ")

# Output file name
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, 'r') as file:
        content = file.read()

    # Convert content to uppercase
    upper_content = content.upper()

    with open(destination_file, 'w') as file:
        file.write(upper_content)

    print("\nFile converted to uppercase successfully!")

    # Display content of both files
    print("\n--- Original File Content ---")
    print(content)

    print("\n--- Uppercase File Content ---")
    print(upper_content)

except FileNotFoundError:
    print("Error: Source file not found.")

Lab Assignment-2

Develop an application using file handling to copy the contents of python script into another without including the comments. Ask the user about the source and destination file names Print the content of the both the files

# Program to copy python file without comments

source_file = input("Enter the source Python file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        stripped_line = line.strip()

        # Ignore full-line comments
        if stripped_line.startswith('#'):
            continue

        # Remove inline comments
        if '#' in line:
            line = line.split('#')[0] + '\n'

        cleaned_lines.append(line)

    # Write cleaned content to destination file
    with open(destination_file, 'w') as file:
        file.writelines(cleaned_lines)

    print("\nComments removed and file copied successfully!")

    # Display both files
    print("\n--- Source File Content ---")
    with open(source_file, 'r') as file:
        print(file.read())

    print("\n--- Destination File Content (Without Comments) ---")
    with open(destination_file, 'r') as file:
        print(file.read())

except FileNotFoundError:
    print("Error: Source file not found.")

