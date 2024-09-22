'''
Decorators are functions that modify the behaviour of other function or methods.
It takes other function as an argument and returns a new function that 
adds some kindof functionality to the original function without 
modifying thier source code.
''' 



'''
Recursion
> Recursion is a programming technique where a function calls itself in order to solve a problem.
> the key to recursion is having a base case, which is a condirion that stops the recursive calls ,
 and a recursive case which is the part where the function calls itself

def fact(n):
    if n == 0 or n==1:
        return n
    else:
        return n * fact(n-1)
    
n=int(input())
reuslt=fact(n)
print(reuslt)


>lambda function  also known as anonymus functions.
>Small,Single expression function defined using the "lambda" keyword
>lambda functions are not intended to be reused multiple times

>they are limited to a single expreddion and cannont contain statements or multiple statements
'''
ADD = lambda x,y: x+y

result = ADD(3,5)
print(f"result : {result}")
 


                                        





