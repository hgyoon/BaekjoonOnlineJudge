'''
#this is the original implementation of counting sort
import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
K = max(arr) # greatest num
count = [0 for a in range(K + 1)]
brr = [0 for b in range(N)]
for i in arr:
    count[i] += 1
for j in range(1, K + 1):
    count[j] += count[j-1]
for l in range(N):
    temp = arr[l]
    count[temp] -= 1
    brr[count[temp]] = temp
for m in brr:
    print(m)
'''

#saving memory~ cuz mr.baekjoon ain't gonna allow much memory
N = int(input())
count = [0 for a in range(10001)]
for _ in range(N):
    count[int(input())] += 1
for j in range(len(count)):
    for l in range(count[j]):
        print(j)
