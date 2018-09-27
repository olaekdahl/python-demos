# nums = [2,5,1,67,1]

# print("before ", nums)

# nums.sort()
# nums.reverse()

# print("after ", nums)

# a = [1, 2, 3, 4, 5, 6]
# b = [5, 6, 7, 8]
# c = list(set(a + b))

# print(c)


a = [1,2,3]
b = (1,2,3)

def get_location():
    long = 0.366363
    lat = 5.66777
    return long, lat

x, y = get_location()

print("long ", x)
print("lat ", y)