class Bank_account():
    def __init__(self, IBAN):
        self.IBAN =  IBAN
        self.balance = 0
    def deposit(self, deposit):
        self.balance += deposit
    def withdraw(self, withdraw):
        if self.balance - withdraw > 0:
            self.balance -= withdraw
        else:
            print("Niewystarczająca ilość środków na rachunku\n")
    def account_status(self):
        print(f"Rachunek nr: {self.IBAN}\nSaldo: {self.balance:.2f} zł\n")
        
bnk = Bank_account("12 3456 5555 9090 1111 0000 7722")
bnk.account_status()
bnk.deposit(25.30)
bnk.account_status()
bnk.withdraw(31.70)
bnk.account_status()
bnk.deposit(14)
bnk.account_status()