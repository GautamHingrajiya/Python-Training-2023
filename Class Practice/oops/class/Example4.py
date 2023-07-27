class BankDemo:

    Balance = 0
    def checkBalance(Self):
        print("Current Balance : ",Self.Balance)

    def Deposit(Self,deopsitamt):
        Self.Balance = Self.Balance + deopsitamt
        print("Deposite Successful.")

    def WithDraw(Self,withdrawamt):
        if withdrawamt < Self.Balance:
            Self.Balance -= withdrawamt
            print("Withdraw Successful.")
        else:
            print("Insufficient Balance")

p = BankDemo() # Object Creation

p.checkBalance() 

deopsitamt= int(input("Enter Amt Want to Deposite : "))
p.Deposit(deopsitamt)
p.checkBalance()

withdrawamt = int(input("Enter Amt Want to Withdraw : "))
p.WithDraw(withdrawamt)
p.checkBalance()