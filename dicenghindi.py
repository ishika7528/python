enhi={'flower':'fool','aeroplane':'jahaaz','clip':'sui'}
hien={'fool':'flower','jahaaz':'aeroplane','sui':'clip'}
dcnry={}
li=[]
for value in hien.values():
    li.append(value)
i=0
for key in enhi:
    dcnry[key]=li[i]
    i=i+1
print(dcnry)
