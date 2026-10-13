words = input("Enter words separated by spaces: ").split()

longest = max(words, key=len)

print("Longest word:", longest)
print("Length of longest word:", len(longest))


# (a) Generate a list of positive numbers
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
positive = [n for n in numbers if n > 0]
print("Positive numbers:", positive)

# (b) Square of N numbers
n = int(input("Enter N: "))
squares = [i * i for i in range(1, n + 1)]
print("Squares:", squares)

# (c) Form a list of vowels from a word
word = input("Enter a word: ")
vowels = [ch for ch in word if ch.lower() in "aeiou"]
print("Vowels:", vowels)

# (d) Ordinal value of each character
word = input("Enter a word: ")
values = [ord(ch) for ch in word]
print("Ordinal values:", values)



d = {}

n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

ascending = dict(sorted(d.items(), key=lambda item: item[1]))
descending = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)




d1 = {}
d2 = {}

n1 = int(input("Enter number of items in dictionary 1: "))

for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

n2 = int(input("Enter number of items in dictionary 2: "))

for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

d1.update(d2)

print("Merged dictionary:", d1)
