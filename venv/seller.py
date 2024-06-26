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
    def add_contract_s(self, contract): #might not have to have self passed as paramater here 
        self.list.append(contract)
        

    def print_seller_contracts(self):
        for x in range(len(self.list)):
            print(self.list[x].__str__())
        # print(self.list)

    @staticmethod
    def sell_contract(self, contract):
        #self.list.remove(contract) -> for the sake of the database, I want to keep the lists intact
        self.rating = self.rating + 1 #add a rating score for each contract that is sold

    def contract_return(self):
        return self.list