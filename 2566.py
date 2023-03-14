a = []
b = []
for i in range(9):
    n = list(map(int, input().split()))
    a.append(max(n))
    b.append(n.index(max(n)))
#biggest num
print(max(a))
idx = a.index(max(a))
print(idx+1, b[idx]+1)