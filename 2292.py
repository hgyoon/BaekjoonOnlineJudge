target = int(input())
i = 1
rooms = 1
while (rooms < target):
    rooms += 6 * i
    i += 1
print(i)