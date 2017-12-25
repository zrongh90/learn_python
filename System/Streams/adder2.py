import sys
sum = 0
while True:
    line = sys.stdin.readline()
    if not line: break
    line_int = int(line.strip())
    sum += line_int
print(sum)
