#Program To Calculate Area of Rectangle
length = input('Enter Length of Rectangle: ');
if length == 'x':
    print('Error!');
else:
    breadth = input('Enter Breadth of Rectangle: ');
    Length = int(length);
    Breadth = int(breadth);
    Area = Length*Breadth;
    print('Area of Rectangle =',Area);
