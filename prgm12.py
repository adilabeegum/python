list1= list(map(int,input("enter 1st list:").split()))
list2= list(map(int,input("enter 2nd list:").split()))
if len(list1)==len(list2):
    print("(a) lists are of the same length")
else:
    print("(a) lists are not of the same length")
if sum(list1)== sum(list2):
    print("(b) lists sum to the same value")
else:
    print("(b) lists do not sum to the same value")
if set(list1).intersection(set(list2)):
    print("(c) both lists contain common value(s)")
else:
    print("(c) no common values")

