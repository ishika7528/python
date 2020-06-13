lst = [('Arnav', ' Bsc', 92), ('ABC', 'Btech', 92.7), ('Aryan', 'BCA', 91), ('CDE', 'Bsc=HM', 82.7)]

for i in lst:
    print(i)
    
n  = input("y/n if you want to change your details : ")
if n == 'y':
    name = input("Enter the name whose details are to be edited : ")
    name2 = input("Enter correct name : ")
    course = input("Enter correct course : ")
    marks = int(input("Enter correct percentage : "))
List1 = [list(x) for x in lst]
print(List1)
for i in range(len(List1)):
    if List1[i][0] == name:
        List1[i][0] = name2
        List1[i][1] = course
        List1[i][2] = marks
print(List1)
