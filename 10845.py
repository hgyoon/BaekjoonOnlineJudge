import sys
N = int(sys.stdin.readline())
stak = []
for i in range(N):
    line = sys.stdin.readline().strip()
    if 'push' in line:
        _, elem = line.split()
        stak.append(elem)
    elif line == 'front':
        if len(stak) == 0:
            print(-1)
        else:
            print(stak[0])
    elif line == 'back':
        if len(stak) == 0:
            print(-1)
        else:
            print(stak[-1])
    elif line == 'size':
        print(len(stak))
    elif line == 'pop':
        if len(stak) == 0:
            print(-1)
        else:
            print(stak.pop(0))
    else:
        if len(stak) == 0:
            print(1)
        else:
            print(0)