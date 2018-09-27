def hello(first_name, last_name):
    return "Hello {0} {1}".format(first_name, last_name)

def line_total(qty, unit_price):
    return qty * unit_price

def main():
    full_name = hello("Ola", "Ekdahl")
    print(full_name)

if __name__ == "__main__":
    main()
