for i in range(int(input())):
    H, W, N = map(int, input().split())
    floor = H if N % H == 0 else N % H
    hosu = N // H if N % H == 0 else (N // H) + 1
    print(floor*100+hosu)