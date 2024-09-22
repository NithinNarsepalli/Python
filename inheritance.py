'''
#1
#single inheritance
class dog():
    def sound(self):
        print("barking")
class puppy(dog):
    def name(self):
        print("i am puppy")
    def sound(self):
        print("bow")
o=puppy()
o.name()
o.sound()

class a():
    def name(self):
        print("a:")
    def add(self):
        print(10+20)
class b(a):
    def name(self):
        print("b:")
    def sub(self):
        print(10-20)
class c(b):
    def name(self):
        print("c:")
o=c()
o.add()
o.sub()
o.name()

# self is a refrerence to the  current instance of the class.
#It is used to acces the variables and methods assoicated with current object

#pass is used for further implementation

#2
#multiple inheritance
class Flyer:
    def flyer(self):
        print("flying")
class Swimmer:
    def swimmer(self):
        print("swimming")
class duck(Flyer,Swimmer):
    pass

o=duck()
o.flyer()
o.swimmer()


#3
#multilevel inheritance
class grandpa:
    def grandpa(self):
        print("Grand Parent")
class parent(grandpa):
    def parent(self):
        print("parent")
class son(parent):
    def son(self):
        print("child")

obj = son()
obj.grandpa()
obj.parent()
obj.son()


#4
#Hiearchial inheritance
class grandpa:
    def grandpa(self):
        print("Grand Parent")
class parent(grandpa):
    def parent(self):
        print("parent")
class son(grandpa):
    def son(self):
        print("child")

obj = son()
obj.grandpa()
obj.son()
obj2 = parent()
obj2.grandpa()
obj2.parent()


#5
#hybrid inheritance
class grandpa:
    def grandpa(self):
        print("Grand Parent")
class grandma:
    def grandma(self):
        print("Grnad Mother")
class parent(grandpa,grandma):
    def parent(self):
        print("parent")
class son(grandpa):
    def son(self):
        print("child")

obj = son()
obj.grandpa()
obj.son()
obj2 = parent()
obj2.grandpa()
obj2.parent()
obj2.grandma()

#method overloading in python

#to do method overloading in python we use meultiple dispatch decorator
#the first implementation is for two int arguments
#the second implementation is for the three int arguments
#third implementation is for the different data type arguments
import multipledispatch
class add:
    @multipledispatch.dispatch(int,int)
    def addition(self,a,b):
        print(a+b)
    @multipledispatch.dispatch(int,int,int)
    def addition(self,a,b,c):
        print(a+b+c)
    @multipledispatch.dispatch(str,str)
    def addition(self,a,b):
        print(a+b)
    @multipledispatch.dispatch(str,int)
    def addition(self,a,b):
        print("Hello "+a,"your score:",b)
o = add()
print("Method Overloading:")
o.addition(1,2)
o.addition(1,2,3)
o.addition("Nithin","Narsepalli")
o.addition("Nithin",75)




#operator overloading

Operator overloading in python allows to define how operations behave with user defined objects.
Example:
print(20+40)
print("hello" +"india")
print([1,2,3] +[4,5,6])

> Python provides a set of special methods for operator overloading
> Also known as magic methods or dunder methods (beacause their names are surrounded by double underscores)
> These methods allow to define how instances if clss behave with operators

'''

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return vector(self.x + other.x,self.y + other.y)
    
v1=vector(1,2)
v2=vector(2,3)
print(v1+v2)





















