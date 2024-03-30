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
        pass
    #start here, need to find a way for the seller to take ownership of the contract 
        #later on buyer will take ownership