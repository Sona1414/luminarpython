class Bank:
    bank="FEDERAL BANK"
    minbal=500
    def account(self,accno):
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))
        self.salary=int(input("Enter the salary"))
        self.type=input("enter the type of account")
        self.accno=accno
        print("Account number:",self.accno)
        self.bal=Bank.minbal
    def deposit(self):
        self.amt=int(input("enter the amount to deposit"))
        self.bal+=self.amt
        print("The current balance is",self.bal)
    def withdraw(self):
        self.amount=int(input("enter the element to withdraw"))
        if self.amount>self.bal:
            print("impossible")
        else:
            self.bal-=self.amount
            print("The current balance is",self.bal)
per1=Bank()
per1.account(10101)
per1.deposit()
per1.withdraw()