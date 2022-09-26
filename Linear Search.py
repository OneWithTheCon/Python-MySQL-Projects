lst=[]
n=int(input('Number of elements in the list: '))
for i in range(0,n,1):
   num=int(input('Enter the items in the list: '))
   lst.append(num)
print (lst)
element=int(input('Enter the element to be searched: '))
pos=-1
for i in range(n):
   if(lst[i]==element):
      pos=i
      break
if (pos== -1):
   print ('Element not found')
else:
   print ('Element found in position',pos+1,'and index',pos)
