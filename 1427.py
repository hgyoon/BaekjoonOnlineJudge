import sys
N = [i for i in sys.stdin.readline()]
N.sort(reverse=True)
for i in N:
    print(i, end="")