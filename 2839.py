N = int(input())

bag_1 = 3
bag_2 = 5
bag_found = []

for i in range(1005):
    for j in range(1700):
        if bag_1 * j + bag_2 * i == N:
            bag_found.append(i+j)

if len(bag_found) == 0:
    print(-1)
else:
    print(min(bag_found))