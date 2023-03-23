N = int(input())
arr = list(map(int,input().split()))
M = int(input())
items = list(map(int, input().split()))

hash_arr = {}

for i in arr:
    if i in hash_arr:
        hash_arr[i] += 1
    else:
        hash_arr[i] = 1

for j in items:
    if j in hash_arr:
        print(hash_arr[j], end = " ")
    else: 
        print(0, end = ' ')