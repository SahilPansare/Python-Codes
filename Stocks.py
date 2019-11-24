class stock:
    def __init__(self,owner,balance=80):
        print("Welcome to Your Stock Warehouse")
        self.owner=owner
        self.balance=balance
        
    def __str__(self):
        return ("Stock is of : {} \nStocks in Warehouse are: {}".format(self.owner,self.balance))
    
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
            print('Remaining stocks are :{}'.format(self.balance))
        else:
            print('stocks Unavailable!')
            
    def alert(self,alert_amt):
        if self.balance<=20:
            print("Supplier should be informed !")
        else:
            print("You still have {} stocks left before informing the supplier".format(abs(20-self.balance)))
 
    
    