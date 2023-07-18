#range(): this finction generate sequence of number between given range.
'''
syntax
range (start, stop, step)
'''
#num=range(1,10,1)
#print(num)

#num=list(range(0,10,1))
#print(num)

#num=list(range(1,10,1))
#print(num)

#num=list(range(1,10,3))
#print(num)    #output =[1, 4, 7]

#num=list(range(1,10,-3))
#print(num)  #output =[]

#num=list(range(1,1,-2))
#print(num)    #output =[]

#num=list(range(1,10)) #DEFAULT VALUE OF STEP IN RANGE IS  1
#print(num)  #output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num=list(range(10))  #DEFAULT VALUE OF START IN RANGE IS  0
print(num)  # OUTPUT= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
