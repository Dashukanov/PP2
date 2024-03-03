#1

import os

def list(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories and Files:")
    for item in os.listdir(path):
        print(item)

specified_path = input()
list(specified_path)



#2

import os

specified_path = input()

if os.path.exists(specified_path):
    print("Path exists.")

    if os.access(specified_path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")

    if os.access(specified_path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")

    if os.access(specified_path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")
else:
    print("Path does not exist.")



#3
import os

def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

given_path = input("Enter the path: ")
check_path(given_path)


#4
def count(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

filename = input()
print(count(filename))


#5
def list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

filename = input()
input_list = input().split()
list_to_file(filename, input_list)
print()

#6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")

generate_files()
print()


#7
def copy(source, dest):
    with open(source, 'r') as sources:
        with open(dest, 'w') as destination:
            destination.write(sources.read())

source_file = input()
destination_file = input()

copy(source_file, destination_file)
print("Success")


#8
import os

def delete(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted")
        else:
            print("No access to the file.")
    else:
        print("File does not exist.")

specified_path = input("Enter the specified path to the file: ")
delete(specified_path)