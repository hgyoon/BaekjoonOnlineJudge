def search(houses, start, end):
    o = 0
    while (start <= end):
        target = (end + start) // 2
        iter = houses[0]
        modem_count = 1 
        for j in range(1, len(houses)):
            if houses[j] - iter >= target:
                iter = houses[j]
                modem_count += 1
        if modem_count >= num_modems_needed:
            start = target + 1
            o = target
        else:
            end = target - 1
    return o

num_houses, num_modems_needed = map(int, input().split())
houses = []
for i in range(num_houses):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1] - houses[0]

print(search(houses, start, end))