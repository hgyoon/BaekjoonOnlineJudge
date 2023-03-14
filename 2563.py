dohwaji = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in range(a, a+10):
        for j in range(b, b+10):
            dohwaji[i][j] = 1
zeros = 0
for i in dohwaji:
    zeros += i.count(1)
print(zeros)