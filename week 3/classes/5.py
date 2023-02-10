class bank:
    def __init__(self, name  , balance = 0 ):
        self.name  = name
        self.balance  = balance
    def plus(self,add):
        self.balance = self.balance+add
        print('balance of',self.name,':',self.balance)
    def denote(self,min):
        if min > self.balance:
            print("balanca ne hvataet")
        else:
            self.balance = self.balance - min
            print('balance of',self.name,':',self.balance)



f = bank('noname',9000)
f.plus(5600)
f.denote(4000)

