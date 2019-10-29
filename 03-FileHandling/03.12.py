while 1:
    with open('shoppinglist.txt','a') as file:
        w=input("Co nalezy dodac do listy zakupow?: ")
        file.write(w)
        file.write("\n")
        while 2:
            x = input("Chcesz jeszcze cos dodac? (t/n): ")
            if x.lower()=="tak" or x.lower()=='t':
                break
            elif x.lower()=="nie" or x.lower()=="n":
                break
            else:
                print("Jesli chcesz jeszcze cos dodac napisz 'tak' lub 't', w przeciwnym przypadku napisz 'nie' lub 'n'")
        if x.lower()=="nie" or x.lower()=="n":
            break
            
