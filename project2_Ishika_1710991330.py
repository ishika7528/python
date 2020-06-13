import pandas as pd
import numpy as np

with open('C:/Users/Ishika Garg/Desktop/Attendance.csv') as file_new:
    df=pd.read_csv(file_new)

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
        'col: 4', 'col: 5', 'col: 6', 'col: 7', 'col: 8',
       'col: 9', 'col: 10', 'col: 11', 'col: 12',
       'col: 13', 'col: 14', 'col: 15', 'col: 16',
       'col: 17', 'col: 18', 'col: 19', 'col: 20',
       'col: 21', 'col: 22', 'col: 23', 'col: 24',
       'col: 25', 'col: 26', 'col: 27', 'col: 28',
       'col: 29', 'col: 30', 'col: 31']
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
   prac_col=df[df.columns[-5:]] 
    
    a2=df1>=0
    a3=prac_col<75
    a4=prac_col>=0
    df2=df[a3&a4]
    df1=df1[a1&a2]
    
    prac_col=df2[df.columns[-5:]]
    
    att1=pd.concat([df['Student Name'],df['Roll_Num'],df['Uni_ID'],prac_col],axis=1)
    
    df.drop(df.iloc[:, 27:31], inplace = True, axis = 1)
    
    att=pd.concat([df['Student Name'],df['Roll_Num'],df['Uni_ID'],df['Total %age'],df1],axis=1)
    
   att.to_csv('C:/Users/Ishika Garg/Desktop/New folder/Attendanceee2.csv',index=False,header=True)
    
att1.to_csv('C:/Users/Ishika Garg/Desktop/New folder/Practicallss2.csv',index=False,header=True)

   
