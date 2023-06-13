class Wallet:
    """
    Class that creates wallets that can spend and add cash
    """
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        """
        Reduces balance by amount and returns new balance.
        If amount is bigger than balanca, withdrawal is denied. 
        """
        if self.balance<amount:
            return 'Not enough money'    
        else:
            self.balance = self.balance - amount
            return f'remaining balance is ${self.balance}'

    def add_cash(self, amount):
        """
        Balance is increased by amount
        ew balance is returned in string
        """
        self.balance = self.balance + amount
        return f'new balance is ${self.balance}'
    
    def __repr__(self):
        return f'Your current balance is ${self.balance}'
