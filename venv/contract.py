#contract

class Contract:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def print_contract(self):
        print(self.price, self.name)

    def get_price(self):
        return self.price
    
    def set_price(self, x):
        self.price = x

    