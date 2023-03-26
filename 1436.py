the_end = []
N = int(input())
i = 1
while len(the_end) < N:
    if '666' in str(i):
        the_end.append(i)
    i += 1
print(the_end[N-1])