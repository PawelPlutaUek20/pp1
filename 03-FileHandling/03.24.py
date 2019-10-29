import csv
dane=['Imie','Nazwisko','Email','Marek','Zalnik','zelnik@sed.pl','Ewa','Maj','maje@wp.pl','Piotr','Wyga','wyga@gop.pl']
with open('plic.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(dane[:3])
    csvwriter.writerow(dane[3:6])
    csvwriter.writerow(dane[6:9])
    csvwriter.writerow(dane[9:12])