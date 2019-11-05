def podatek(dochod):
    if dochod<=5000:
        podatek=17/100*dochod
    elif dochod>5000:
        podatek=50*17+((dochod-5000)*32/100)
    print('Podatek nalezny: %d zł' % podatek)
input_dochod=int(input('Podaj dochod: '))
podatek(input_dochod)
