#Binary Operations
import pickle
import os
s={}
def main():
    print('1.Write data to file')
    print('2.Read data from file')
    print('3.Appending record')
    print('4.Search record')
    print('5.Updation of record')
    print('6.Deletion of record')
    print('7.Exit')


def write_data():
    f=open('student.dat','wb')
    while True:
        s['roll']=int(input('Enter roll'))
        s['name']=input('Enter name')
        s['marks']=int(input('Enter marks'))
        pickle.dump(s,f)
        print('Record written')
        ch=input('Do you want to insert more records(Y/N) ')
        if upper(ch)=='N':
            break
    f.close()
def read_data():
        f=open('student.dat','rb')
        f.seek(0)
        try:
            while True:
                s=pickle.load(f)
                print(s)
        except Exception:
            f.close()
        

def append_rec():
    f=open('student.dat','ab')
    while True:
        s['roll']=int(input('Enter roll'))
        s['name']=input('Enter name')
        s['marks']=int(input('Enter marks'))
        pickle.dump(s,f)
        print('Record appended')
        ch=input('Do you want to insert more records(Y/N) ')
        if upper(ch)=='N':
            break
    f.close()

def search_rec():
    f=open('student.dat','rb')
    r=int(input('Enter the roll to be displayed'))
    f.seek(0)
    found=False
    try:
      while True:
        s=pickle.load(f)
        if(s['roll']==r):
              found=True
              print(s)
    except Exception:
            f.close()
        

def update_rec():
    f=open('student.dat','rb+')
    f.seek(0)
    r=int(input('Enter the roll of the record to be updated'))
    try:
        while True:
            pos=f.tell()
            s=pickle.load(f)
            if s['roll']==r:
                s['name']=input('Enter name')
                s['marks']=int(input('Enter marks'))
                f.seek(pos)
                pickle.dump(s,f)
                print('Record updated')
    except Exception:
         f.close()
            
def del_rec():
   f=open('student.dat','rb')
   f1=open('temp.dat','ab')
   r=int(input('Enter the roll to be deleted'))
   f.seek(0)
   try:
      while True:
        s=pickle.load(f)
        if(s['roll']==r):
              continue
        pickle.dump(s,f1)
   except Exception:
            f.close()
            f1.close()
   os.remove('student.dat')
   os.rename('temp.dat','student.dat')
   print('Record deleted')         
        
while True:
    main()
    ch=int(input('Enter your choice'))
    if ch==1:
        write_data()
    elif ch==2:
        read_data()
    elif(ch==3):
        append_rec()
    elif(ch==4):
        search_rec()  
    elif(ch==5):
        update_rec()
    elif(ch==6):
        del_rec()
    else:
        break
