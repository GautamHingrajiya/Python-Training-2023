class bank:
    balance = 100
    def cashDeposite(self,deposite):
        self.balance = self.balance + deposite

        return self.balance
    
    def cashWithdraw(self , withdraw):
        if withdraw > self.balance:
            return "Insufficiant Balance"
        else:
            self.balance -= withdraw
            return self.balance
        
    def showBalance(self):

        return self.balance
    

transection = bank()

print(transection.showBalance())
            