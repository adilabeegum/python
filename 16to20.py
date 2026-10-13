color_list1 = input("Enter colors for list 1: ").split(",")
color_list2 = input("Enter colors for list 2: ").split(",")

print("Colors not present in list 2:")
for color in color_list1:
    if color not in color_list2:
        print(color)



colors = input("Enter comma-separated colors: ").split(",")

print("First color:", colors[0])
print("Last color:", colors[-1])



numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

result = []
for n in numbers:
    if n % 2 != 0:
        result.append(n)

print("List after removing even numbers:", result)


string = input("Enter a string: ")

for ch in string:
    if string.index(ch) == string.find(ch):
        print(ch, ":", string.count(ch))


string = input("Enter a string: ")

if len(string) < 3:
    result = string
elif string.endswith("ing"):
    result = string + "ly"
else:
    result = string + "ing"

print("Result:", result)
