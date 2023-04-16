# import sys
# while True :
#     a = sys.stdin.readline().rstrip()
#     stack = []
#     if a == "." :
#         break
#     balanced = 'yes'
#     # if a[-1] != ".":
#     #     balanced = 'no'
#     for i in a :
#         if i == '[' or i == '(' :
#             stack.append(i)
#         elif i == ']' :
#             if len(stack) != 0 and stack[-1] == '[' :
#                 stack.pop()
#             else : 
#                 stack.append(']')
#                 balanced = 'no'
#                 break
#         elif i == ')' :
#             if len(stack) != 0 and stack[-1] == '(' :
#                 stack.pop()
#             else :
#                 stack.append(')')
#                 balanced = 'no' #this doesn't care [[ or [(
#                 break
#     print(balanced)
import sys
while True :
    a = sys.stdin.readline().rstrip()
    stack = []
    if a == "." :
        break
    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')