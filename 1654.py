def cut_using_m(m, arr_k):
    count = 0
    for i in arr_k:
        temp = i
        while (m <= temp):
            temp -= m
            count += 1
    return count


N, K = map(int, input().split())
arr_k = []
for i in range(N):
    arr_k.append(int(input()))

low = 1
high = 2**31 - 1
mid = (low+high) // 2  # int((low+high)/2)

while (low <= high):
    # print(low, high)
    if cut_using_m(mid, arr_k) >= K:  # success
        low = mid + 1
    else:
        high = mid - 1
    mid = (low+high) // 2

print(mid)
