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
    #second seller
    Jen = Seller('Jen', 5)
    #print(Lucas.get_rating())  #show the rating of a seller

    #instantiate Buyer
    Henry = Buyer('Hentry', 5)

    #add a contract to a seller
    Seller.add_contract_s(Lucas, mid_size_SUV)

    #2 more contracts
    modern_home = Contract(214000, 'modern_home')
    equipment_lease = Contract(22399, 'bottle_maker')

    #add 2 new contracts to Jen
    Seller.add_contract_s(Jen, modern_home)
    Seller.add_contract_s(Jen, equipment_lease)

    #Lucas.print_seller_contracts()  #this is working but only prints the memory address
    
    #Henry will buy the contract off Lucas
    Buyer.buy_contract(Henry, Lucas, mid_size_SUV)
    
    # Henry.print_buyer_contracts()   #contract at 0x7fa5ab5573a0>
    # Lucas.print_seller_contracts()  #nothing 
    
   # Jen.print_seller_contracts() #working

    #Henry will buy the contracts off Jen and display them
    Buyer.buy_contract(Henry, Jen, modern_home)
    Buyer.buy_contract(Henry, Jen, equipment_lease)
    
    print('All of Henrys contracts')
    Henry.print_buyer_contracts()

    print('Henry drops the car contract')

    Henry.drop_contract(mid_size_SUV)
    Henry.print_buyer_contracts()




    #maybe look into adding bidding