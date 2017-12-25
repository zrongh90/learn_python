import sys
lines = sys.stdin.readlines()
lines_int = [ int(num) for num in lines ]
for one_int in lines_int:
    print(type(one_int)," =>  ", one_int)
print("sum of this is ", sum(lines_int))
