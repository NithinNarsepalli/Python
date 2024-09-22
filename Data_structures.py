'''
###############################list
l=[1,2,"nithin","raju"]
l.pop()
print(l)
l.pop(1)
print(l)
l.append("raju")
print(l)
l[1]=2
print(l)
l1=[12,10,4,5]
l1.sort()
print(l1)
l2=l1.copy()
print(l2)
l1.insert(2,"ganesh")
print(l1)

#tuples
t1 = (1,2,3)
print(t1)
print(t1[1])
print(max(t1))
print(min(t1))
t2=(9,8,10)
t2=t1+t2

print(t2)

s="red"
my_t= tuple(s)
print(my_t)



#set
set1={1,2,1,3,4,5}
set2={1,2,3,3,6}
a=set1.union(set2)
print(a)
b=set1.intersection(set2)
print(b)
c=set1.symmetric_difference(set2)
print(c)
d=set1.difference(set2)
print(d)

#
d={1:"raj",
   2:"nithin",
   3:"get"}
d[1]=("ganesh")
print(d)
d.insert(4,"jiya")


#string
k="ramu naidu"
print(k[1])
print(k.upper())
print(k.lower())
print(k.strip())
print(k.split())
print(k.title())
print(k.capitalize())

# global and local variable demonstration
x=10
def outer():
      x=20
      def  inner():
         nonlocal x
         x=30
         print("inner",x)
      inner()
      print("outer",x)
outer()
print("global",x)
'''


x=10
def outer():
      global x, y
      def  inner():
         nonlocal x
         x=30
         print("inner",x)
      inner()
      print("outer",x)
outer()
print("global",x)

























