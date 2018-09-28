import os
import platform
from os import listdir
from os.path import isfile, join
import time
from datetime import date, datetime, timedelta
#mypath = "C:\\Users\\ISInc\\Desktop\\python"

def pause():
    programPause = input("Press the <ENTER> key to continue...")

print("!!!The Word Finder!!!")
print("******************************************")
print()

while True:
    path = input("Enter folder path: ")
    in_date = input("Enter date (MM/DD/YYYY): ")
    dt = datetime.strptime(in_date, "%m/%d/%Y")
    file_date = date(dt.year, dt.month, dt.day)

    try:

        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        break
    except FileNotFoundError as e:
        print(e)
        print("Please try again...")

print("Enter search word.")
print("******************************************")
print()

search_word = input("Key word or sentence: ")
matching_files = []
# matching_files[["file1.txt", 2], ["file2.txt", 5]]

counter = 1
for file in onlyfiles:
    full_path = join(path, file)
    creation_datetime = datetime.strptime(time.ctime(os.path.getctime(full_path)), "%a %b %d %H:%M:%S %Y")

    creation_date = date(creation_datetime.year, creation_datetime.month, creation_datetime.day)

    if creation_date == file_date: 
        word_counter = 0
        with open(full_path, "r") as file:
            data = file.readlines()
            if any(search_word in l for l in data):
                for line in data:
                    if search_word in line:
                        word_counter += 1
                file_info = [file.name, word_counter]
                matching_files.append(file_info)

print("Matching files:")
print("Total number of matching files: ", len(matching_files))
print()

for match in matching_files:
    print("File: {0}. Word Mathces: {1}".format(match[0], match[1]))


print()
pause()