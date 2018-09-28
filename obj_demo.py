from objects import Product

apple = Product("Green Apple", .099)
banana = Product("Lettuce", .89, "produce")

fruit = [apple, banana]

def print_prod_info(fruit):
    print(fruit.name)

for f in fruit:
    print_prod_info(f)

