import sys
N = int(sys.stdin.readline())
line = sys.stdin.readline().strip()
output = 0
for i in range(N):
    output += (ord(line[i])-96) * (31**i)
print(output % 1234567891)