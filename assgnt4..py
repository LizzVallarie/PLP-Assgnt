import os

def generate_output_filename(input_filename):
    """
    Generate the output filename by inserting '_modified' before the extension.
    For example, 'example.txt' becomes 'example_modified.txt'.
    """
    root, ext = os.path.splitext(input_filename)
    return f"{root}_modified{ext}"

def modify_line(line):
    """
    Modify the line by converting it to uppercase.
    """
    return line.upper()

def main():
    # Prompt the user for the input filename
    input_filename = input("Enter the filename to read: ")
    
    # Generate the output filename based on the input filename
    output_filename = generate_output_filename(input_filename)
    
    try:
        # Open the input file for reading with UTF-8 encoding
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            # Open the output file for writing with UTF-8 encoding
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                # Process the file line by line
                for line in input_file:
                    # Modify each line and write it to the output file
                    modified_line = modify_line(line)
                    output_file.write(modified_line)
        # Inform the user of success
        print(f"Successfully wrote modified content to {output_filename}")
    
    except FileNotFoundError:
        # Handle the case where the input file doesn’t exist
        print(f"Error: The file '{input_filename}' does not exist.")
    
    except PermissionError:
        # Handle the case where there’s a permission issue with either file
        print(f"Error: Permission denied to read '{input_filename}' or write to '{output_filename}'.")
    
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()