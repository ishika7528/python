a=input("enter list")
l1=a.split()
l2=[]
for i in range(0,len(l1)):
    r=l1[i].capitalize()
    b=r[-1]
    d=r[0:len(r)-1]
    print(d+b.capitalize(),end=" ")
