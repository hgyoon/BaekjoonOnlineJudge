def sosueyo(num):
    sosuya = False
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            sosuya = True
    return sosuya
a = int(input())
b = int(input())
sosu = []
sosu_hap = 0
for i in range(a, b+1):
    if sosueyo(i) == True:
        sosu.append(i)
        sosu_hap += i
if (len(sosu) != 0):
    print(sosu_hap)
    print(min(sosu))
else:
    print(-1)