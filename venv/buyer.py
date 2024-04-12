from seller import Seller
from contract import Contract

class Buyer:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.held_contracts = []

    def get_rating(self):
        return self.rating
    
    def set_rating(self, x):
        self.rating = x

    @staticmethod
    def buy_contract(self, Seller, Contract) :
        Seller.sell_contract(Seller, Contract) #contract should be removed from the seller array list
        self.held_contracts.append(Contract) #contract should add itself to the array list of the buyer


        #04.11.24 working!

        #more complex ideas later
        #find the seller that has the contract
        #take the contract away from the seller array list and 
        #add it to the buyers arrary list 

        #we could put in a conditional that finds the matching contract from the seller
        #and takes it out and puts in the buyers array

        #start here**
        #if Seller.contract_return() ==     
                #could loop through the seller's array list of contracts and once the matching one is found, remove it from seller and add it to seller. 
        

    def print_buyer_contracts(self):
        print(self.held_contracts)