import csv
dane=[['Marek','Zalnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wyga@gop.pl']]
dane2=['Imie','Nazwisko','Email']
with open('plic.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(dane2)
    csvwriter.writerow(dane[0][:])
    csvwriter.writerow(dane[1][:])
    csvwriter.writerow(dane[2][:])