hakjum_sum = 0.0
score_sum = 0.0
score = {
    'A+':	4.5,
    'A0':	4.0,
    'B+':	3.5,
    'B0':	3.0,
    'C+':	2.5,
    'C0':	2.0,
    'D+':	1.5,
    'D0':	1.0,
    'F' :	0.0,
}
while (True):
    try:
        a, b, c = input().split()
        if c != 'P':
            score_sum += float(score[c]) * float(b)
            hakjum_sum += float(b)
    except:
        break

print('% 6f' % (score_sum / hakjum_sum))