def create_file():
    """Creates a new text file and writes initial content."""
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("Here is the second line, and a number: 75.\n")
            file.write("Finally, this is the third line.\n")
        print("File created and content written successfully.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")
    
    finally:
        print("Create file operation finished.")


def read_file():
    """Reads and displays the content of the text file."""
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile Contents:")
            print(content)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    
    finally:
        print("Read file operation finished.")


def append_to_file():
    """Appends additional content to the existing text file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending this new line 1.\n")
            file.write("Appending another line with number: 300.\n")
            file.write("This is the last appended line.\n")
        print("Additional content appended successfully.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")

    finally:
        print("Append file operation finished.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  
