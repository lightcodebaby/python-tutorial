import os
import shutil

path = "./test.txt"

# Check if a path exists, and if it's a file or a folder

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")

# Read files

try:
    with open("./test.txt") as file:
        print(file.read())
    print(file.closed)
except FileNotFoundError:
    print("That file was not found")

# Write files

text = "Hello world!\nWe are writting this from Python script!"

with open("./test.txt", "a") as file:
    file.write(text)

# Copy files

shutil.copyfile("./test.txt", "./test-copy.txt")

# Move files

source = "./test.txt"
destination = "/Users/ruben.lopez/Documents/test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

# Delete files

path = "./test.txt"

try:
    os.remove(path)
    os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You dont have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")
