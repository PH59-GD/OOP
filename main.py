mylist = [2, 56, 43, 18, 29, 9]
mylist.append(66)
mylist.remove(56)
mylist.pop() #Removes the last element of the list
mylist.sort()
newlist = mylist.copy()
newlist.append(1001)
print(newlist)
print(mylist)
for n in mylist:
    print(n)