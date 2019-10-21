#24
cm = float(input("Podaj swoj wzrost: "))
inch = cm/2.54
ft=int(inch/12)
rin=inch-ft*12
print("Mam {:.0f} cm wzrostu, tj. {} stóp i {:.0f} cali.".format(cm,ft,rin))