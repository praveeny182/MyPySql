import pickle
from prettytable import PrettyTable
import os
from pathlib import Path
'''l=[1,2,3]
#file='my.pkl'
#fileobj=open(file,'wb')
#pickle.dump(l,fileobj)
#fileobj.close()

file='my.pkl'
fileobj=open(file,'rb')
l=pickle.load(fileobj)
print(l)'''
def helpme():
    
    print(f'''Python sql discription:
          -->Creat=[crt]       
          
          -->Dispaly=[dsp]     
          
          -->Update=[ud] 
          
          -->Help=[H]
          
          -->Sort=[sort]
          
          -->Insert Data in The Table=[Insert]
          
          -->Show List Of Table=[lt]
          
          -->Delete Table=[dlt]
          
          --> Merge On Basis Of Foreign key=[fk]
          
          >>exit=[exit]
          
          
         ''')
def database(file,table_value):
    #print(os.getcwd())
    try:
        #root = Path('C:/Users/praveen/Desktop/MyPySQL')
        #my_path = root / "database" / file
        fileobj=open(file,'wb')
        pickle.dump(table_value,fileobj)
        fileobj.close()
    except:
        print(f"      ---Unsuccessfull---      ")
def option():
    print(f'''Python sql discription:
          -->Creat=crt
          -->dispaly=dsp
          -->update=ud
          -->help=helpme
          -->sort=sort
          -->insert
          -->show list of table=ltable
          -->delete table=dlt
          --> Merge On Basis Of Foreign key=fk
          >>exit=exit
          
         ''')
def readdatabase(table):
    try:
        file=table
        #root = Path('C:/Users/praveen/Desktop/MyPySQL')
        #my_path = root / "database" / file
        fileobj=open(file,'rb')
        tmp_table=pickle.load(fileobj)
        return tmp_table
    except:
        print(f"      ---fail---      ")
def tmp_display(tmp_table_1):
    t = PrettyTable(tmp_table_1[0])
    for i in range(1,len(tmp_table_1)):
        t.add_row(tmp_table_1[i])
    print(t)
    
def display():
    try:
        print("[Display Mode]Enter Table Name >>",end=" ")
        table=input()
        table+='.pkl'
        file=table
        fileobj=open(file,'rb')
        tmp_table=pickle.load(fileobj)
        t = PrettyTable(tmp_table[0])
        for i in range(1,len(tmp_table)):
            t.add_row(tmp_table[i])
        print(t)
        '''for i in tmp_table:
                for j in i:
                    print(j,end="  ")
        print()'''
        fileobj.close()
    except:
        print(f"          ---Wrong Table Name---         ")
def show_meta():
    try:
        print(f'       ---List Of Tables---        ')
        fileobj=open('meta_tb.pkl','rb')
        mt_tb=pickle.load(fileobj)
        print(mt_tb) 
    except:
        print("---No table---")
    
    
def meta_table(table):
    try:
        fileobj=open('meta_tb.pkl','rb')
        print(fileobj)
        mt_tb=pickle.load(fileobj)
        fileobj.close()
        if table not in mt_tb:
            mt_tb.append(table)
            fileobj=open('meta_tb.pkl','wb')
            pickle.dump(mt_tb,fileobj)
            fileobj.close()
            return True
        else:
            print("Table Already Present In DataBase")
            return False
        
        
    except:
        mt_tb=[table]
        fileobj=open('meta_tb.pkl','wb')
        pickle.dump(mt_tb,fileobj)
        fileobj.close()
        return 
def delete():
    try:
        print("[Delete Mode]Enter Table Want To Delete >>",end=" ")
        table=input()
        table+='.pkl'
        tmp_table=readdatabase('meta_tb.pkl')
        tmp_table.remove(table)
        database('meta_tb.pkl',tmp_table)
        print("[Delete Mode]Successfully Deleted")
    except:
        print(f"      ---Wrong Input---      ")
    
def insert():
    try:
        print("[Insert Mode]Enter Table Name >>",end=" ")
        table=input()
        table+='.pkl'
        tmp_table=readdatabase(table)
        #print(tmp_table)
        if tmp_table:
            print(tmp_table[0])
            print("[Insert Mode]Inter Values And For Exit(out) >>")
            while True:
                l=list(input().split())
                if l==['out']:
                    break
                tmp_table.append(l)
            database(table,tmp_table)
            print("[Insert Mode]insert successfully") 
        else:
            print("[Insert Mode]Wrong Table")
    except:
        print("[Insert Mode]WRONG INPUT")
def add_table(table1,table2,key):
    x=len(table1[0])
    y=len(table2[0])
    x1=x+y-1
    mx_len=max(len(table1),len(table2))
    l=[[0]*x1]*mx_len
    print(l)
    for i in range(mx_len):
        for j in range(x1):
            if j<x:
                l[i][j]=table1[i][j]
                print(l[i][j],end=" ")
            elif j-x<y and table2[0][j-x]!=key and i<len(table2):
                l[i][j]=table2[i][j-x]
                print(l[i][j],end=" ")
            else:
                print(l[i][j],end=" ")
        print()
                
    tmp_display(l)
    
            
        
        
        
    
def Foreign():
    print("Enter First Table Name >>",end=" ")
    table1=input()
    print("Enter Sec. Table Name >>",end=" ")
    table2=input()
    print("Enter Foreign Key >>",end=" ")
    key=input()
    table1+='.pkl'
    table2+='.pkl'
    tmp_table1=readdatabase(table1)
    tmp_table2=readdatabase(table2)
    print(tmp_table1[0])
    add_table(tmp_table1,tmp_table2,key)
    '''print("Want To Result Will Be A New Table yes or no>>")
    ans=input()
    if ans=='yes':
        print("Enter New Table Name >>")
        tab=input()
        tab+='.pkl'
        database(tab,tmp_table1)
        meta_table(tab)
    print("Want To See yes or no >>")
    ans1=input()
    if ans1=='yes':
        tmp_display(tmp_table1) '''              
    
def srt():
    try:
        print("[Sort Mode]Enter Table Name >>",end=" ")
        table=input()
        table+='.pkl'
        tmp_table_1=readdatabase(table)
        tmp_table=tmp_table_1[1::]
        print("[Sort Mode]On The Basis Of CLM No. >>",end=" ")
        cl_no=int(input())
        print("[Sort Mode]Sorting ASC or DSC >>",end=" ")
        tmp_cmd=input()
        if tmp_cmd=='asc':
            tmp_table=sorted(tmp_table,key=lambda x:x[cl_no])
        elif tmp_cmd=='dsc':
            tmp_table=sorted(tmp_table,key=lambda x:x[cl_no],reverse=True)
        for i in range(1,len(tmp_table_1)):
                       tmp_table_1[i]=tmp_table[i-1]
        #print(tmp_table_1)
        print("[Sort Mode]Want Also Update In Database yes or no >>",end=" ")
        s=input()
        if s=='yes':
            database(table,tmp_table_1)
            print("[Sort Mode]Sucessfully Update")
        print("[Sort Mode]Display Table yes or no >>",end=" ")
        pm=input()
        if pm=='yes':
            tmp_display(tmp_table_1)
        
    except:
        print("[Sort Mode]Wrong Entry")
        
        
    
    
def update():
    try:
        print("[Update Mode]Enter Table Name >>",end=" ")
        table=input()
        table+='.pkl'
        file=table
        fileobj=open(file,'rb')
        tmp_table=pickle.load(fileobj)
        while True:
            print("[Update Mode]No oF Coloum And No of Row Number >>",end=" ")
            clm_name,row=map(int,input().split())
            print("[Update Mode]New Value:",end=" ")
            tmp_table[row][clm_name]=input()
            print("[Update Mode]If Want More Update Type yes or no >>",end=" ")
            ans=input()
            if ans=="no":
                break
        
        database(file,tmp_table)
        print("[Update Mode]Table Successfully Update")
    except:
        print("[Update Mode]Wrong Entry")

def creat():
    try:
        print("[Creat Mode]Enter Table Name:",end=" ")
        table_name=input()
        print()
        table_name+='.pkl'
        if meta_table(table_name):
            file=table_name
            print("[Creat Mode]Enter Number Of Coloum:",end=" ")
            clm=int(input())
            if clm>0:
                table_value=[[0 for x in range(clm)] for x in range(1)]
                #print(table_value)
                print("[Creat Mode]Enter Coloum Name:")
                #table_value.append(list(input().split()))
                #print("Enter coloum name and press enter:",end=" ")
                for i in range(clm):
                        table_value[0][i]=input()
                #print("Enter data value:")
                #for i in range(1,row+1):
                        #table_value[i]=[0]*clm
                database(file,table_value)
                print("[Creat Mode]Table succuessfully Created")
                
            else:
                print("[Creat Mode]Colom Must Be Greater Than Zero")
        else:
            print("Table Name must be uniqe")
    except:
        print("[Creat Mode]Wrong Entry")
                
    
             
if __name__=="__main__":
    print(f'''Python sql discription:
          -->Creat=[crt]       
          
          -->Dispaly=[dsp]     
          
          -->Update=[ud] 
          
          -->Help=[h]
          
          -->Sort=[sort]
          
          -->Insert Data in The Table=[Insert]
          
          -->Show List Of Table=[lt]
          
          -->Delete Table=[dlt]
          
          --> Merge On Basis Of Foreign key=[fk]
          
          >>exit=[exit]
          
          
         ''')
    while True:
        print("Enter Your Command >>",end=" ")
        cmd=input()
        if cmd=='crt':
            creat()
        elif cmd=='exit':
            print("Done")
            break
        elif cmd=='dsp':
            display()
        elif cmd=='ud':
            update()
        elif cmd=='h':
            helpme()
        elif cmd=='sort':
            srt()
        elif cmd=='insert':
            insert()
        elif cmd=='lt':
            show_meta()
        elif cmd=='dlt':
            delete()
        elif cmd=='op':
            option()
        elif cmd=='fk':
            Foreign()
            
        else:
            print(f"    ---Cmd Is Wrong Again Type---      ")



