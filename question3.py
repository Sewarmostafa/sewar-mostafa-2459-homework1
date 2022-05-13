q="E://f.txt"
user=input('enter your name')
file=open(q, 'r')
s=file.read()
l=s.splitlines()
i=0
x=0
for x in range(20):
    w=input(l[x][0])
    if w==l[x][1]:
        i+=1
print(user,i)
d=open("E://e.txt",'w')
a=[user,str(i)]
d.writelines(a)
d.close()




