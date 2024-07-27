# import pandas as pd
# #df holds a dataframe object
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
# # variable that form part of an object are called attribute
# if __name__ == '__main__':
#     df.shape
#     df.columns
#     df.index
#     df.dtypes
#     df.columns 
#     # function  that form part of an object called method
#     df.head()
#     print(df.describe())
class Wallet:
    def __init__(self, initial_amount):
        #save the user -provided initial_amount as an atribute
        #'self' refers to what ever object i am working
        self.balance = initial_amount
    def spend_cash(self, amount):
        if self.balance < amount:
            return 'not enough money'
        else: 
            return 'remaining balance: {self.balance}'
    def add_cash(self, amount):
        self.balance += amount
        return f'new balance of {self.balance}'
    
    def __repr__(self):
        return f'wallet with balance of: {self.balance}'
        
if __name__ == '__main__':

    wallet1 = Wallet(100)
    print(wallet1.spend_cash(200))