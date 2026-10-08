text=input("enter a line of text:")
words=text.split()
count={}
for word in words:
   if word in count:
     count[word]+=1
   else:
     count[word]=1
print(count)
