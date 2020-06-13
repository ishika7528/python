a=int(input("enter amount"))
if(a<=150000):
    print("tax=0")
elif(a>150000 and a<=300000):
    i=a-150000
    t=0.10*i
    print("tax=",t)
elif(a>300000 and a<=500000):
    i=a-150000
    if(i<=300000):
        t=i*0.10
        print("tax=",t)
     else(i>300000):
         e=i-300000
         t=
