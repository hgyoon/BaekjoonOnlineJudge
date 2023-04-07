'''
import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
# arr.sort()
arr.sort(key=lambda x:(x[1],x[0]))
for elem in arr:
    print(elem[0],elem[1])
'''
import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
for elem in sorted(arr, key=lambda y:(y[1],y[0])):
    print(elem[0],elem[1])