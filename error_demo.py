try:
    num = float(input("Enter a number: "))
    print("You entered ", num)
except ValueError as e:
    print("oops! ", e)
    raise e
except OSError:
    print("something else!")