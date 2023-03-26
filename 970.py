N = int(input())
D = 0
P = 0
for _ in range(N):
    if D - P == 2 or P - D == 2:
        break
    if input() == 'D':
        D += 1
    else:
        P += 1
print(str(D)+":"+str(P))