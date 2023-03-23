N = int(input())
arr = list(map(int, input().split()))
M = int(input())
items = list(map(int,input().split()))
arr.sort()
for i in items:
    found = 0
    low = 0
    high = len(arr) - 1
    mid = int((low + high) / 2)
    while(low <= high):
        # print("i", i, "arrmid",arr[mid])
        if i == arr[mid]:
            found = 1
            break
        if i > arr[mid]:
            low = mid + 1
        else :
            high = mid - 1
        # print('low',low,'high',high)
        mid = int((low + high) / 2)
    print(found)