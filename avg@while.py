a=input("input a number")
p=0
n=0
s1=0
s2=0
while(a!="@"):
    a=int(a)
    if(a>=0):
        s1=s1+a
        p=p+1
    else:
        s2=s2+a
        n=n+1
    a=input()
print("positive,negative, are :",s1/p,s2/n)
