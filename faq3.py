s=input("enter string")
a1=input("enter start")
a2=input("enter end")
l=len(s)
f=s.index(a1)
g=s.index(a2)
count=0
a=" "
for i in range(f,g+1):
    a=a+s[i]
    count=count+1
    print(a)
print(count)
    
        
       
