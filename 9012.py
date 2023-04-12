#parenthesis (())()()()
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    line = sys.stdin.readline().strip()
    left = []
    right = []
    for i in line:
        if i == '(':
            left.append(i)
        else:
            if len(left) != 0:
                left.pop()
            else:
                right.append(i)
    if len(left) == 0 and len(right) == 0:
        print("YES")
    else:
        print("NO")
