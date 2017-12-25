import sys
print('Got this: %s' % input())
mydata = sys.stdin.readline()[:-1]
print('The meaning of life is {} {}'.format(int(mydata), int(mydata) * 2))
