n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
for _ in range(m):
    begin, end, mid = map(int, input().split())
    front_part = arr[mid-1:end]
    end_part = arr[begin-1:mid-1]
    arr[begin-1:end] = front_part + end_part
for i in arr:
    print(i, end=" ")
