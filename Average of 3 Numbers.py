#Program To Print the Average of 3 Numbers
print('Enter Any 3 Numbers To Find Their Average: ');
n1 = input()
if n1 == 'x':
   print('Error!');
else:
    n2 = input();
    n3 = input();
    number1 = int(n1);
    number2 = int(n2);
    number3 = int(n3);
    sum = number1 + number2 + number3;
    Average = sum/3;
    print('Average Of The 3 Numbers Is = %0.2f'%Average);
