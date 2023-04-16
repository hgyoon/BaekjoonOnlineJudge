import sys
K = int(sys.stdin.readline())
stack = []
sum = 0
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
for i in stack:
    sum += i
print(sum)