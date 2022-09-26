#Program To Calculate Area of Triagle
base = input('Enter Base of Triangle: ');
if base == 'x':
    print('Error!');
else:
    height = input('Enter Height of Triangle: ');
    Base = int(base);
    Height = int(height);
    Area = 0.5*Base*Height;
    print('Area of Triangle =',Area);
