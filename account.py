class Account:
    # Constructor 
    def __init__(self, username, password, balance):
        # Variables
        self.username = username
        self.password = password
        self.balance = balance
        self.dict = {}
        
    def serialize(self):
        self.dict = {
            "Name": [self.username],
            "Password": [self.password],
            "Balance": [self.balance]
        }
        
        return self.dict
