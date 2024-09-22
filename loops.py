'''
i = 0
while i <= 10:
    print(i)
    i+=1

#printing the next three vallues from the given value.
i = int(input("value:"))
count=0
while(count<3):
    count+=1
    i+=1
    print(i)

#odd number from 1 to 10
i=1
while(i<=10):
    if(i %2 !=0):
        print(i)
    i += 1

#printing the three numbers from the given value
a=int(input())
for i in range(a+1,a+4):
    print(i)

#accepting the values 3 values from the user and checking whether 
#the given last two values summation is divisible by the first value or not

a = int(input("divisible:"))
b = int(input("value:"))
c = int(input("value:"))
d=b+c
if(d % a==0):
    print(a)




count=0
for i in range(1,11):
    count+=1
print("number of count:",count)



#counting the digits in the given range
count=0
s=0
k=0
for i in range(10,16):
    print(i)
    s  = len(str(i))
    k  = s+k
    count += 1  
print()
print(k)
print(count)





a = int(input())
b = int(input())


_-------------------------
a = int(input())
p = int(input())
res=0
for i in range(1,p+1):
    if(i % 2 !=0):
        res= -a ** i
        print("iteration:",i,"negative:",res)
    elif(i % 2 ==0):
        res = a ** i
        print("iteration:",i,"positive:",res)

#*****
*****
*****
*****
*****   
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()


    
#pattern
*
**
***
****
*****

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
'''
'''
* * * * * 
* *     * 
*   *   * 
*     * * 
* * * * * 


n=5
for i in range(n):
    for j in range(n):
        if i == 0 or j== 0 or i == n-1 or j == n-1 or j==i :
            print("*",end=" ")
        else:
            print(" ",end =" ")
    print()
    
'''


