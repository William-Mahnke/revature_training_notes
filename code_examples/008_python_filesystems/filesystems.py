# Opening files using try/except/finally block. 
# Note: This is not the recommended approach - instead use 'with' statements
file = None
try:
    file = open("python_filesystems/data.txt", "r", encoding="utf-8")
    print(file.tell())      # index Starts at 0
    content = file.read()   # read the contents
    print(file.tell())      # final character index
    file.seek(0)            # reset to initial index
    first_line = file.readline()    # read a single line
    print(f"first line: {first_line}")
    print(f"file Content:\n{content}")
except FileNotFoundError:
    print("File does not exist")
finally:
    if file != None:
        file.close()

# Append Mode:
print(" ### APPEND MODE ###")
with open("python_filesystems/data.txt", "a") as f:
    f.write("\nThis is my new line - line 4")

with open("python_filesystems/data.txt", "r") as f:
    content = f.read()
    print(f"file Content:\n{content}")


# Write Mode (Overwrites Files):
print(" ### WRITE MODE (OVERWRITING EXISTING FILE) ###")
with open("python_filesystems/data.txt", "w") as f:
    f.write("I'm replacing the content in this file")

with open("python_filesystems/data.txt", "r") as f:
    content = f.read()
    print(f"file Content:\n{content}")

# utility function to reset data.txt file:
def reset_data_file():
    print("Resetting the Data File")
    with open("python_filesystems/data.txt", "w") as f:
        f.write("This is line 1\nThis is line 2\nThis is line 3\n")
reset_data_file() # Calling this just to reset the file back to original state

# Use 'x' (exclusive create) over 'w' to handle new file creation
print(" ### EXCLUSIVE CREATE MODE ###")
try:
    with open("python_filesystems/data.txt", "x") as f:
        f.write("I'm creating a new file")
except (FileExistsError):
    print("File already exists")

with open("python_filesystems/data.txt", "r") as f:
    content = f.read()
    print(f"file Content:\n{content}")


# 'w' creates the file if it doesn't exist, overwrites if it does
file_path = "python_filesystems/demo.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello, this is line 1\n")
    f.write("Hello, this is line 2\n")
    f.write("Hello, this is line 3\n")

print("--- After WRITE (create new file) mode ('w') ---")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())

# 'a' preserves existing content and adds to the end
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Hello, this is line 4 (appended)\n")
    f.write("Hello, this is line 5 (appended)\n")

print("--- After APPEND mode ('a') ---")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())

# 'r+' opens for both reading and writing — file must already exist
# The cursor starts at the BEGINNING of the file
with open(file_path, "r+", encoding="utf-8") as f:
    content = f.read()                            # Read all existing content
    modified = content.replace("Hello", "Hi")     # Modify the content
    f.seek(0)                                     # Rewind cursor to start
    f.write(modified)                             # Overwrite with modified content
    f.truncate()                                  # Remove any leftover characters

print("--- After READ+WRITE mode ('r+') ---")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())



# Binary mode — for non-text files
with open("python_filesystems/logo.jpg", "rb") as f:  # Read binary
    data = f.read()

with open("python_filesystems/logo-copy.png", "wb") as f:   # Write binary
    f.write(data)
