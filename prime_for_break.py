#prime number=number that is completely divisible by 1 and itself
'''
n=int(input("enter the number:"))
for i in range(2,n):
    r=n%i
    if r==0:
        print("non prime number")
        break
    
#output= enter the number:24
         non prime number
'''
'''
n=int(input("enter the number:"))
for i in range(2,n):
    r=n%i
    if r==0:
        print("non prime number")
        break
    else:
        print("prime number")
#output=enter the number:14
       non prime number
 '''
n=int(input("enter the number:"))
for i in range(2,n):
    r=n%i
    print(i)
    if r==0:
        print("non prime number")
        break
    else:
        print("prime number")
