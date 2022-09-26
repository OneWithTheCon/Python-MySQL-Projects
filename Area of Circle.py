#Program to Print Area of Circle
radius = input('Enter The Radius Of The Circle: ');
if radius == 'x':
    print('Error!');
else:
    Radius = float(radius);
    Area = 3.14*Radius**2;
    print('Area of Circle = π*Radius^2 = %0.2f' %Area);
