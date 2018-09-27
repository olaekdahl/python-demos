import utils

print("Enter quantity and unit price")
qty =  int(input("Quantity :"))
unit_price = float(input("Unit price :"))

total = utils.line_total(qty, unit_price)

print(total)
