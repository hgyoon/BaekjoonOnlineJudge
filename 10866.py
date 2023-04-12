import sys
N = int(sys.stdin.readline())
stak = []
for i in range(N):
    line = sys.stdin.readline().strip()
    if 'push_back' in line:
        _, elem = line.split()
        stak.append(elem)
    elif 'push_front' in line:
        _, elem = line.split()
        temp = []
        temp.append(elem)
        if len(stak) != 0:
            for i in range(1, len(stak)+1):
                temp.append(stak[i-1])
        stak = temp
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
    elif line == 'pop_front':
        if len(stak) == 0:
            print(-1)
        else:
            print(stak.pop(0))
    elif line == 'pop_back':
        if len(stak) == 0:
            print(-1)
        else:
            print(stak.pop())
    else:
        if len(stak) == 0:
            print(1)
        else:
            print(0)