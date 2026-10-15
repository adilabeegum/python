n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b



numbers = list(map(int, input("Enter list items: ").split()))
total = 0

for n in numbers:
    total = total + n

print("Sum =", total)


import math

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

for n in range(max(start, 1000), min(end, 9999) + 1):
    root = math.isqrt(n)

    if root * root == n and all(int(d) % 2 == 0 for d in str(n)):
        print(n)



n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
