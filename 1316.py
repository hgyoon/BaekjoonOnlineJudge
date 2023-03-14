#simple solution
n = int(input())
count = n
for i in range(n):
    a = input()
    b = []
    current = ''
    identifier = True
    for j in a:
        if current != j and j not in b:
            current = j
            b.append(j)
        elif current != j and j in b:
            identifier = False
    if identifier == False:
        count -= 1
print(count)