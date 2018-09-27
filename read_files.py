import os
from os import listdir
from os.path import isfile, join
#mypath = "C:\\Users\\ISInc\\Desktop\\python"

def pause():
    programPause = input("Press the <ENTER> key to continue...")

print("!!!The File Reader!!!")
print("******************************************")
print()

while True:
    path = input("Enter folder path: ")

    try:
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        break
    except FileNotFoundError as e:
        print(e)
        print("Please try again...")

print("Pick a file to open.")
print("******************************************")
print()

counter = 1
for file in onlyfiles:
    print(str(counter) + ": ", file)
    counter += 1

print()
file_number = int(input("Enter number to open file: "))
print()
print()

file = join(path, onlyfiles[file_number-1])

with open(file, "r") as file:
    for line in file.readlines():
        print(line.replace("\n",""))
print()
pause()