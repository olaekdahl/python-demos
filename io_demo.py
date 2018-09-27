# outfile = open("test.txt", "a")
# outfile.write("some text\n")
# outfile.close()

# outfile = open("test.txt", "r")
# data = outfile.read()
# outfile.close()

# print(data)

# with open("test.txt", "r") as file:
#    for line in file.readlines():
#        print(line.replace("\n", ""))

# import csv

# items = [["CEO","Ola"],["Mgr","Fred"],["Sales","Tim"]]

# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(items)


# import csv
# with open("people.csv", newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         print(', '.join(row))

# import pickle

# data = [["CEO","Ola"],["Mgr","Fred"],["Sales","Tim"]]

# with open("data.bin", "wb") as datafile:
#     pickle.dump(data, datafile)

# with open("data.bin", "rb") as datafile:
#     data = pickle.load(datafile)

# print(data)





