import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

avg = 0
median = 0
r = 0
f = Counter(arr).most_common(2)
print(f)

for i in range(N):
    avg += arr[i]
avg /= N
print(round(avg))

median = arr[N // 2]
print(median)

if N > 1:
    print(f[1][0]) if f[0][1] == f[1][1] else print(f[0][0])
else:
    print(f[0][0])

range = arr[-1] - arr[0]
print(range)