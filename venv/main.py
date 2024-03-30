from contract import Contract
from seller import Seller

class main:
    def __init__(self) -> None:
        pass
        
    mid_size_SUV = Contract(45000, 'car') #make contracts
    #Contract.print_contract(first_customer) #display contracts

    #instantiate seller
    Lucas = Seller('Lucas', 3)
    #print(Lucas.get_rating())  #show the rating of a seller

    #add a contract to a seller
    Seller.add_contract_s(Lucas, mid_size_SUV)

    Lucas.print_seller_contracts()  #this is working what only prints the memory address
    
    
    
    
    #what do we want to do?
    #have a buyer and seller -> probably need classes
    #contract class
    #marketplace -> bidding, buying and selling occur -> add and subtract contracts from here. 