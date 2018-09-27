# outfile = open("test.txt", "a")
# outfile.write("test data from a Python\n")
# outfile.close()
input_file = "test.txt"
current_dir = __file__ #remove filename
current_dir = current_dir.replace("io_demo2.py",input_file)
# file_name = current_dir + "\\" + input_file
# test
with open(current_dir, "r") as file:
    for line in file.readlines():
        print(line.replace("\n",""))

# print(__package__)


# nums = [1,2,3]

# with open("test.txt", "w") as file:
#     for num in nums:
#        file.write(str(num) + "\n")


people = [["CEO","Anna"],["Sales","Tim"],["Mgr","Fred"]]

import pickle
# with open("data.bin", "wb") as datafile:
#     pickle.dump(people, datafile)

# with open("data.bin", "rb") as datafile:
#     data = pickle.load(datafile)
# print(type(data))

# import csv

# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(people)

# with open("people.csv", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(" | ".join(row))

