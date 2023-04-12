N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
a_out = []
idx = K - 1
for j in range(N):
    if idx >= len(arr):
        idx = (idx % len(arr))
    a_out.append(arr.pop(idx))
    # print(idx, a_out)
    idx += K - 1
print("<",end='')
print(*a_out, sep=', ', end='')
print(">",end='')

'''
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
print("<",end="")
idx = K - 1
for j in range(N):
    if idx >= len(arr):
        idx = (idx % len(arr))
    print(arr.pop(idx), end="")
    if len(arr) != 0:
        print(', ',end="")
    # print(idx, a_out)
    idx += K - 1
print(">")
'''