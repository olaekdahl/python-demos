from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN 

balance = 100.10
balance += 100.10
balance += 100.10
print(round(balance,2))

balance = Decimal("100.10")
balance += Decimal("100.10")
balance += Decimal("100.10")

print(balance)

balance = Decimal("100.01240")

print(balance.quantize(Decimal("1.0000"), ROUND_HALF_DOWN))
print(balance.quantize(Decimal("1.0000"), ROUND_HALF_UP))
print(balance.quantize(Decimal("1.0000"), ROUND_HALF_EVEN))