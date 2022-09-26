#Program To Print the Smallest of 'n' Numbers
print('Program To Print the Smallest of \'n\' Numbers')
i=int(input('Enter\'n\'limit: '))
small=int(input('Enter a Number in the set: '))
n=1
n=n+1
while n<=i:
    num=int(input('Enter a Number in the set: '))
    if small>num:
        small=num
    n=n+1
print('The Smallest Number in',i , 'numbers is', small)
print("-----------------------------------")

#Program To Check the Entered Number is Prime or Not
print('Program To Check the Entered Number is Prime or Not')
divisor=0
n=int(input('Enter a Number: '))
i=1
while i<=n:
    if n%i==0:
        divisor=divisor+1
    i=i+1    
if divisor<=2:
    print('The Number is PRIME')
else:
    print('The Number is NOT PRIME')
print("-----------------------------------")

#Program To Find the Sum of Digits of a Given Number
print('Program To Find the Sum of Digits of a Given Number')
num = int(input("Enter any Number: "))
Sum = 0
while(num>0):
    Reminder=num%10
    Sum=Sum+Reminder
    num=num//10
print("Sum of the Digits of Given Number = %d" %Sum)
print("-----------------------------------")

#Program To Check if the Entered Number is a Palindrome or Not
print('Program To Check if the Entered Number is a Palindrome or Not')
num=int(input('Enter a Number: '))
n=num
pal=0
while n>0:
    digit=n%10
    pal=pal*10+digit
    n=n//10
if num==pal:
    print("Number", num, "is a Palindrome")
else:
    print("Number", num, "is not a Palindrome")
print("-----------------------------------")

#Program to Reverse a Number
print('Program to Reverse a Number')
num = int(input("Please Enter any Number: "))
Reverse = 0
while(num>0):
    Reminder = num%10
    Reverse = (Reverse*10)+Reminder
    num = num//10

print("Reverse of Number is = %d" %Reverse)
print("-----------------------------------")

#Program To Print Fibonacci Series upto n
print('Program To Print Fibonacci Series upto n')
n=int(input('Enter\'n\'limit: '))
x=0
y=1
z=1
print(x)
print(y)
while z<=n:
    print(z)
    x=y
    y=z
    z=x+y
print("-----------------------------------")
    
    
    
    

