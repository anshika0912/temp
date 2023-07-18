#number raised to power
num=int(input("enter the number:"))
power=int(input("enter power"))
t=1
for power in range(power,0,-1):
 t=t*num
print(t)
