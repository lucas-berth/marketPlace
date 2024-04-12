from contract import Contract
from seller import Seller
from buyer import Buyer

class main:
    def __init__(self) -> None:
        pass
        
    mid_size_SUV = Contract(45000, 'car') #make contracts
        #this will probably be made through an uploaded csv later on.
    #Contract.print_contract(first_customer) #display contracts

    #instantiate seller
    Lucas = Seller('Lucas', 3)
    #print(Lucas.get_rating())  #show the rating of a seller

    #instantiate Buyer
    Henry = Buyer('Hentry', 5)

    #add a contract to a seller
    Seller.add_contract_s(Lucas, mid_size_SUV)

    #Lucas.print_seller_contracts()  #this is working but only prints the memory address
    
    #Henry will buy the contract off Lucas
    Buyer.buy_contract(Henry, Lucas, mid_size_SUV)
    
    Henry.print_buyer_contracts()   #contract at 0x7fa5ab5573a0>
    Lucas.print_seller_contracts()  #nothing 
    

    
    #what do we want to do?
    #have a buyer and seller -> probably need classes
    #contract class
    #marketplace -> bidding, buying and selling occur -> add and subtract contracts from here. 