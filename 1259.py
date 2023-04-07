import sys
while(True):
    word = sys.stdin.readline().strip()
    if word == "0":
        break
    else:
        i = 0
        j = len(word) - 1
        palindrome = True
        while (i <= j):
            if word[i] != word[j]:
                palindrome = False
                break
            i += 1
            j -= 1
        print('yes') if palindrome == True else print('no')