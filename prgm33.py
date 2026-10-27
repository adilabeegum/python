n=int(input("enter a no:"))
temp =n
power=len(str(n))
total=0
while temp>0:
  digit=temp%10
  total=total + digit ** power
  temp =temp//10
if total ==n:
  print("armstrong no")
else:
  print("not an armstrong no")
