def czytajTekst():
    with open('C:/Users/Paweł/Desktop/pp1/05-ModularProgramming/spendings.txt', 'r') as file:
        tekst = file.read()
        return tekst

tekst=czytajTekst()
def pobierzDane():   
    import re
    dane=[]
    x = re.findall('(?<!\d)\d{3}[0-9]?(?!\S)|(?<!\d)\d(?!\S)|(?<!\d)\d{3}[0-9]?\.\d{2}(?!\S)', tekst)
    for num in x:
            dane.append(float(num))
    return dane