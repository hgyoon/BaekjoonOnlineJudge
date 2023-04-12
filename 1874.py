import sys
NUM_LINE = int(sys.stdin.readline())
num = 1
sequence = []
solution = []
possible = True

for _ in range(NUM_LINE):
    target = int(sys.stdin.readline())
    while num <= target:
        sequence.append(num)
        solution.append("+")
        num += 1
    if sequence[-1] != target:
        possible = False
        break
    else:
        sequence.pop()
        solution.append("-")

print("\n".join(solution)) if possible else print("NO")
