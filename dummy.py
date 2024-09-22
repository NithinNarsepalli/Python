'''
def checknum(s):
    for i in s:
        if i.isnumeric():
            print("True")
    
print(checknum("ab4"))

#stack demonstration
stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
print()
popped=stack.pop()
print(popped)
print()
print(stack)


#queue demonstration
queue = []
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)
print()
popped=queue.pop(0)

print(popped)
print()
print(queue)

#function
def solve(s):
    if 0<len(s)<1000:
        res= s.split(" ")
        resul=" "
        for i in range(len(res)):
            resul = resul+res[i].capitalize()
        return resul
'''
import copy
original_list=[[1,2],[1,2]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)
original_list[0][1]=9
print(original_list)
print(shallow_copy)
print(deep_copy)
 









#shallow copy -> copy.copy()




