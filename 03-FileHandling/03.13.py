tablica = [32,16,5,8,24,7]
with open("Tablica.txt", 'a') as file:
    for a in tablica:
        file.write(str(a)+'\n')