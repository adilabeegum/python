numbers = list(map(int, input("Enter list items: ").split()))
total = 0

for n in numbers:
    total = total + n

print("Sum =", total)
