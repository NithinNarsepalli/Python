a=[1,2,3]
try:
    print(a[4])
except(IndexError):
    print("IndexError")
else:
    print("else")
finally:
    print("program at finally")
