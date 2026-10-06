numbers = list(map(int,input("enter integers separated by space:").split()))
for i in range(len(numbers)):
   if numbers[i]>100:
      numbers[i]="over"
print(numbers)
