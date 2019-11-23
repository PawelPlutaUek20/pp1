def transportyzacja(macierz):
    tab_tr=[]
    tab_tred=[]
    k=0
    for x in macierz:
        pass
    for i in range(len(x)):
        for j in macierz:
            tab_tr.append(j[k])
        k+=1
        tab_tred.extend([tab_tr])
        tab_tr=[]
    for y in tab_tred:
        print(*y, sep=' ')
macierz=[[1,2,0],[0,0,3],[5,1,1]]
transportyzacja(macierz)
