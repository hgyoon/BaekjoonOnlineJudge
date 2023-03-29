N = int(input())
arr = [int(input()) for _ in range(N)]
for i in range(N-1):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
for k in arr:
    print(k)
