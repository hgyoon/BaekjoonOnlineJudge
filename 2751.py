import sys
arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
arr.sort()
for i in arr:
    print(i)
