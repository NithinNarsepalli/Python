#iter
#next
#an iterator is an object that contains a countable number of values.
#they implement the iterator protocol which requires two methods:__iter__() and __next__()
#iterators are used to iterate over containers like list,tuples,dictionaries and sets
#to create an object/class as an iterator we have to implement the methods __iter__() and __next__() to your object.
#the __iter__() method acts as similar 



'''
a=[1,2,3]
b=iter(a)
b.next()
print(next(b))
print(next(b))
print(next(b))


s="nithin"
b=iter(s)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#generator 

> Generators are a special type iterator that generator values lazilly.
> they are defined using a function with the "yeild" keyword instead of return
> generators are memory efficient because they produce values on the fly



#fibbonaci series
def fibbonaci(n):
    if n<0:
        print("Invalid Input")
    elif(n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:
        yield fibbonaci(n-1)+fibbonaci(n-2)
    
print(fibbonaci(10))


##################
def fibo(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
n=int(input())
fib_seq = fibo(n)
for num in fib_seq:
    print(num,end=' ')


#factorial
def fact(n):
    if n==0:
        return n
    else:
        fac=1
        for i in range(1,n+1):
            fac *= i
    return fac

print(fact(5))
#factorial

def fact(n):
    if n == 0 or n==1:
        return n
    else:
        return n * fact(n-1)
    
n=int(input())
reuslt=fact(n)
print(reuslt)
'''








