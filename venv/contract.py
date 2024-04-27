#contract

class Contract:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    @staticmethod
    def print_contract(self):
        print(self.price, self.name)

    @staticmethod
    def get_price(self):
        return self.price
    
    @staticmethod
    def set_price(self, x):
        self.price = x
    
    @staticmethod
    def get_name(self):
        return self.name

    def __str__(self):
        return f' The contract consists of {self.name} at {self.price}'