from contract import Contract

class Seller:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.list = []  #try this method, otherwise set the list only inside the add_contract method

    def get_rating(self):
        return self.rating
    

    def set_rating(self, x):
        self.rating = x

    @staticmethod   #this allows us to use the method without using the object itself
    def add_contract_s(self, contract):
        self.list.append(contract)

    def print_seller_contracts(self):
        print(self.list)