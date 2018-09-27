from decimal import Decimal

balance = Decimal("100.10")
balance += Decimal("100.10")
balance += Decimal("100.10")

print(balance)

msg = "Hello {0} from {1}".format("Ola", "Sac")
