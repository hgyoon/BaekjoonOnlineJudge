# dynamic approach time exceeded sibal!
# def lower(floor, hosu):
#     if (floor < 2):
#         return sum(range(1,hosu+1))
#     else:
#         total = 0
#         for i in range(1, hosu+1):
#             total += lower(floor-1, i)
#         return total

def lower(floor, hosu):
    apatu = [i for i in range(1, hosu+1)]
    for i in range(floor):
        for j in range(1, hosu):
            apatu[j] += apatu[j-1]
    return(apatu[-1])
    

for i in range(int(input())):
    floor = int(input())
    hosu = int(input())
    print(lower(floor = floor, hosu = hosu))