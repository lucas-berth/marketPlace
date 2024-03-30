from contract import Contract

class Seller:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def get_rating(self):
        return self.rating
    

    def set_rating(self, x):
        self.rating = x


    def own_contract(self):
        