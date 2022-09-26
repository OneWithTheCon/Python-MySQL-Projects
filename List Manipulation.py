#Program for List Rotation
lst=[]
#Appending the Elements
l=int(input("Enter the size of the List: "))
print("Enter the number:")
for i in range(int(l)):
   p=int(input("n="))
   lst.append(int(p))
print (lst)
#Rotation of Elements  
r = 1 #Number of Rotations Change value for multiple rotations
lst = (lst[-r:] + lst[:-r])
print("After Rotation",lst)
