def msg(name, age=30, location="Sacramento"):
    age += 10
    return "Hello {0} from {1}. In 10 years you will be {2} years old".format(name, location, age)

# thsi is atest
if __name__ == "__main__":
    print("Please enter info.")
    print()

    name = input("Enter name: ")
    location = input("Enter location: ")
    age = int(input("Enter age: "))

    output = msg(name)
    
    print(output)
