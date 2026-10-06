names=input("enter 1st names separated by space:").split()
count=0
for name in names:
 count+=name.lower().count('a')
print("no of occurrences of 'a':",count)
 
