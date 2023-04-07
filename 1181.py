'''
strip() was used to get rid of "\n"s at the end of each lines
implementation without using set() and sort(key = len)
'''


'''
import sys
N = int(sys.stdin.readline())
words = [[] for _ in range(0,51)]
for _ in range(N):
	word = sys.stdin.readline().strip()
	if word not in words[len(word)-1]:
	    words[len(word)-1].append(word)
for i in words:
    i.sort()
for j in words:
	if len(j) != 0:
	    for k in j:
	        print(k)
'''
'''


import sys
N = int(sys.stdin.readline())
words = [[] for _ in range(0, 51)]
for _ in range(N):
    word = sys.stdin.readline().strip()
    if word not in words[len(word)-1]:
        words[len(word)-1].append(word)
for i in words:
    i.sort()
    if len(i) != 0:
        for j in i:
            print(j)
'''

import sys
N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(N)]
words = list(set(words))
words.sort(key = lambda x: (len(x), x))
for j in words:
	print(j)