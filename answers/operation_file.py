try:
    # Opening the input file for reading
    with open("target_file.txt", "r") as file:
        content = file.read()

    # Modifying the content by converting to uppercase
    modified_content = content.upper()

    # Checking if the output file already has content
    try:
        with open("output.txt", "r") as file:
            # Strip to remove leading/trailing whitespace
            existing_content = file.read().strip()
    except FileNotFoundError:
        existing_content = ""  # If file doesn't exist, assume it's empty

    # Write or append the modified content to the output file
    with open("output.txt", "a") as file:
        if existing_content:
            # Append with a new line if file has content
            file.write("\n" + modified_content)
        else:
            file.write(modified_content)  # Write directly if file is empty

    print("Content has been successfully written to 'output.txt'.")

except FileNotFoundError:
    print("Error: 'target_file.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Error Handling
filename = input("Enter the filename to read: ")

try:
    # Open the specified file for reading
    with open(filename, "r") as file:
        content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
