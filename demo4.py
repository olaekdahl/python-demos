name = "Fred"

TAX_RATE = 2.4


def TAX_RATE2():
    return 2.4

TAX_RATE = 2.6

print("1. name="+name)

def test(name):
    #global name
    name = "Tim"
    print("2. name="+name)

test("Ola")

print("3. name="+name)
