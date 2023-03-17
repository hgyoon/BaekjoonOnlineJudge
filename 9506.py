while(True):
    try:
        a = int(input())
        if a == -1:
            break
        yaksu = []
        addall = 0
        for i in range(1, a):
            if a % i == 0:
                yaksu.append(i)
                addall += i
        # print(addall, yaksu)
        if addall == a:
            dohagi = ' + '.join('{}'.format(i) for i in yaksu)
            print(str(a) + ' = ' + dohagi)
        else:
            print(str(a) + ' is NOT perfect.')
    except:
        break