a=input("enter paranthesis")
li=a.split(" ")

for i in range(0,len(li)):
    if(a[i]=='(' or a[i]=='[' or a[i]=='{'):
        for j in range(i,i+1):
            if(a[i+1]==')' or a[i+1]==']' or a[i+1]=='}'):
                print("true")
    else:
        print("false")
        

