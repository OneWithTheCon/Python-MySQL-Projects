import csv
def main():
    print('1.Write data to file')
    print('2.Read data from file')
    print('3.Count the number of records')
    print('4.Search record')
    print('5.Selecting record from file')
    
    
#Writer
def write_rec():
    f=open('CS.csv','w',newline='')
    sw=csv.writer(f)
    sw.writerow(['Roll','Name','Marks'])
    record=[]
    while True:
        roll=int(input('Enter roll no: '))
        name=input('Enter name: ')
        marks=int(input('Enter marks: '))
        record=[roll,name,marks]
        sw.writerow(record)
        ch=input('Do you want to continue(Y/N) ')
        if ch in 'Nn':
            break
    f.close()
#Reader   
def read_rec():
    f=open('CS.csv','r')
    sw=csv.reader(f)
    for i in sw:
        print(i)
    f.close()

#Count
def count_rec:
    f=open('CS.csv','r')
    sw=csv.reader(f)
    c=0
    for i in sw:
        c=c+1
        print('The number of records are', c)
    f.close()

def search_rec:
    f=open('CS.csv','r')
    sw=csv.reader(f)
    name=input('Enter the name to be searched: ')
    for row in sw:
        if row[2]==name:
            print('Search Successful; Record Found')
            print(row)
    f.close()
    
def select_rec():
    f=open('CS.csv','r')
    sw=csv.reader(f)
    n=input('Enter the record number/Roll No: ')
    for line in sw:
        print(line[n])
    f.close()

while True:
    main()
    ch=int(input('Enter your choice'))
    if ch==1:
        write_rec()
    elif ch==2:
        read_rec()
    elif(ch==3):
        count_rec()
    elif(ch==4):
        search_rec()  
    elif(ch==5):
        select_rec()
