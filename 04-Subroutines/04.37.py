tab=[0,0,423,42,432,5,3,-1,2,0,42,8]
new_tab=[]
def dont_repeat():
    for i in tab:
        if tab.count(i)==1:
            new_tab.append(i)
    print(new_tab)
dont_repeat()