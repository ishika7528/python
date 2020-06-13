y=int(input("enter a year"))
if((y%4==0) or ((y%400==0) and (y%100!=0))):
    print("it is a leap year")
else:
    print("not a leap year")
