min = 1
#row is our row of the pyramid
row = 1
n = int(input())
while(True):
    if min <= n and n < min+row:
        break
    else:
        min += row
        row += 1
# print('min ',min,'row ',row)
diff = n - min
direction = (row % 2)
top = 0
bot = 0
if direction == 0:
    top = 1 + diff
    bot = row - diff
else:
    top = row - diff
    bot = 1 + diff
print("%d/%d" % (top,bot))