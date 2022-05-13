f=int(input('enter the decimal number'))
l=[]
while f!=0:
    x=f%2
    l.append(x)
    f=f//2
l.reverse()
print(l)






