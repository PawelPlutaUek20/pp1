jezyki=['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosci=[61000,47000,37000,31000,26000,18000,14000,14000,9000,7000]
def rysujWykres(jezyki,wartosci):
    for i in jezyki:
        print('%10s:'%i, end=' ')
        for j in wartosci:
            print('#'*(j//1000))
            wartosci.remove(j)
            break
rysujWykres(jezyki,wartosci)