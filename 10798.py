max_length = 0
lengths = []
agg = []
for _ in range(5):
    n = input()
    if (max_length < len(n)):
        max_length = len(n)
    agg.append(n)
#agg[0][1] works!
new_word = ""
for i in range(max_length):
    for j in range(len(agg)):
        if i < len(agg[j]):
            new_word += agg[j][i]
print(new_word)