#Program for bubble sort
lst=[]
while True:
    num=int(input('Enter element'))
    lst.append(num)
    ch=input('Continue(Y/N)')
    if(ch!='Y' and ch!='y'):
        break
print(lst)
n = len(lst)
for i in range(n): # Number of passes
    for j in range(0, n-i-1): # size ‐i‐1 because last i elements are already sorted
        if lst[j] > lst[j+1] :
            lst[j], lst[j+1] = lst[j+1], lst[j]
print('The sorted list is')
print (lst )
