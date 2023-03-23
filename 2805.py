def cut_tree(h, arr_N):
    offset = 0
    for i in arr_N:
        if i >= h:
            offset += i - h
    return offset

N, M = map(int, input().split())
arr_N = list(map(int, input().split()))

min = 0
max = max(arr_N)
mid = int((min+max)/2)

while min <= max:
    # print('min: ',min, 'mid: ',mid, 'max: ',max)
    temp = cut_tree(mid, arr_N)
    # print('temp:', temp)
    if  temp < M:
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min+max)/2)
print(mid)