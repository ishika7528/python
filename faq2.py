n=int(input("enter number of flowers"))
lis=[]
for i in range(n):
    f=int(input("enter number of flowes"))
    if f not in lis:
        lis.append(f)
print(lis)
