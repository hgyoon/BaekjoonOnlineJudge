N = int(input())
arr = list(map(int, input().split()))
M = int(input())
items = list(map(int, input().split()))

hash_dict = {}

for i in arr:
    if i in hash_dict:
        hash_dict[i] += 1
    else:
        hash_dict[i] = 1

for j in items:
    if j in hash_dict:
        print(hash_dict[j], end=" ")
    else:
        print(0, end=' ')
