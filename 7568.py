import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    arr.append([A, B])
for i in range(N):
    standing = 1
    for j in range(N):
        x, y = arr[i]
        p, q = arr[j]
        if x < p and y < q:
            standing += 1
    print(standing, end = " ")