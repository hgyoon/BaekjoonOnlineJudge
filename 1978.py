N = int(input())
num_list = list(map(int, input().split()))
total_sosu = 0
for num in num_list:
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            total_sosu += 1
print(total_sosu)