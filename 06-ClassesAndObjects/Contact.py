class Kontakt():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def show_contact(self):
        print(f'{self.name:<15} {self.email:<15} {self.phone}')

class ListaKontaktów():
    def __init__(self):
        self.contacts = []

    def add_contact(self, *args):
        for contact in args:
            self.contacts.append(contact)

    def show_contacts(self):
        for contact in self.contacts:
            contact.show_contact()         

n1 = Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000')
n2 = Kontakt('Borek Patrycja', 'bp@o2.pl', '232000199')
n3 = Kontakt('Maj Piotr', 'maj@google.pl', '222999100')
n4 = Kontakt('Adamczyk Anna', 'ada@poczta.pl', '100200300')
lista = ListaKontaktów()
lista.add_contact(n1,n2,n3,n4)
lista.show_contacts()