# a = input()
# count = 0
# i = len(a) - 1
# while(i >= 0):
#     if a[i] == '-':
#         i -= 1
#     elif a[i] == '=':
#         i -= 1
#         if a[i] == 'z':
#             i -= 1 
#     elif a[i] == 'j':
#         if i != 0:
#             if a[i-1] == 'l' or a[i-1] == 'n':
#                 i -= 1
#     count += 1
#     i -= 1
# print(count)

a = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    a = a.replace(i, '+')
print(len(a))