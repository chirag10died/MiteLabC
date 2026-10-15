def listsum(list_1):
    t=0
    for n in list_1:
        t+=n
    return t
list_1=[]
for i in range(10):
    a=int(input("Enter the numbers:"))
    list_1.append(a)
print(list_1)
print(listsum(list_1))
