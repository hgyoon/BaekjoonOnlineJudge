a_1, a_0 = map(int, input().split())
c = int(input())
n = int(input())
print('1') if (a_1*n+a_0) <= (c*n) and c >= a_1 else print('0')