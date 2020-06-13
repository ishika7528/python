# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

with open('C:/Users/Ishika Garg/Desktop/Attendance.csv') as file_obj:
    df=pd.read_csv(file_obj)
    
    df['Ã¯Â»Â¿For Time Table']=df['Ã¯Â»Â¿For Time Table'][4:]
    
    df.dropna(subset=['Ã¯Â»Â¿For Time Table'],inplace=True)
    
    df.dropna(subset=['NVU-Odd Sem'],inplace=True)
    
    df.index = np.arange(1,len(df)+1)
    
    a='Ã‚Â'
    
    str1='Ã¯Â»Â¿For Time Table'
    
    for i in df['Ã¯Â»Â¿For Time Table']:
    
        if a in i:
            i=i.replace(a,'')
    
    df.columns=['Serial Number', 'Roll_Num', 'Uni_ID', 'Student Name',
        'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8',
       'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12',
       'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16',
       'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20',
       'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24',
       'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28',
       'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31']
    
    cols_to_check=df.columns[4:]
    
    df[cols_to_check]=df[cols_to_check].replace({ 'Ã‚Â' : ''},regex=True)
    
    df[cols_to_check]=df[cols_to_check].replace({ '---' : -1},regex=True)

    df['Serial Number']=df['Serial Number'].str[4:]
    
    df['Serial Number'].iloc[0]='Serial Number'
    
    df['Unnamed: 31'].iloc[0]='Total %age'
    
    lst=[]
    
    for i in range(0,32):
        lst.append(df.iloc[0][i])
    
    new_header = df.iloc[0] 
    
    df = df[1:] 
    
    df.columns = new_header
    
    df.reset_index(drop=True,inplace=True)
    
    df.columns=df.columns.str.strip()
    
    df.drop(df.tail(1).index,inplace=True)
    
    df['AML3201']=df['AML3201'].astype(float)
    
    df.iloc[:,4:32]=df.iloc[:,4:32].astype(float)
    
    df1=df[df.columns.difference(['Serial Number',  'Roll_Num', 'Uni_ID', 'Student Name','Total %age'])]
    
    practicalcolumn=df[df.columns[-5:]]
    
    f1=df1<75
    f2=df1>=0
    f3=practicalcolumn<75
    f4=practicalcolumn>=0
    df2=df[f3&f4]
    df1=df1[f1&f2]
    
    practicalcolumns=df2[df.columns[-5:]]
    
    res1=pd.concat([df['Student Name'],df['Roll_Num'],df['Uni_ID'],practicalcolumns],axis=1)
    
    df.drop(df.iloc[:, 27:31], inplace = True, axis = 1)
    
    res=pd.concat([df['Student Name'],df['Roll_Num'],df['Uni_ID'],df['Total %age'],df1],axis=1)
    
    res.to_csv('C:/Users/Ishika Garg/Desktop/New folder/Attendance.csv',index=False,header=True)
    
    res1.to_csv('C:/Users/Ishika Garg/Desktop/New folder/Practicallss.csv',index=False,header=True)

