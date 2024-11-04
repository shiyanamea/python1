mylist=list(map(int,input("enter the elements:").split())
total=0
print(mylist)
for i in range(0,len(mylist)):
    total=total+mylist[i]
print("sum of list",total)
