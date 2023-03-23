n = int(input())
# print(sum(range(n-1))+sum(range(n-1))+(n-2))

# sum = 0
# num = n-2
# for i in range(1, n-1):
#   sum += (num * i)
#   num -= 1
# print(sum)
# print(3)

sum = 0
for i in range(1, n-1):
    print("i")
    for j in range(i+1, n):
        print("j")
        for k in range(j+1, n+1):
            print("k = ", sum, "")
            sum += 1
            # print(sum)
