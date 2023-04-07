'''
#implementing queue but time limit exceeded
N = int(input())
cards = list(range(1, N+1))

while (len(cards) > 1):
    cards.pop(0)
    cards.append(cards.pop(0))

print(cards.pop(0))
'''

from collections import deque
N = int(input())
cards = deque(list(range(1, N+1)))

while (len(cards) > 1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards.popleft())