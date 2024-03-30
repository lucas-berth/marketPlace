from contract import Contract

class main:
    def __init__(self) -> None:
        pass
        
    first_customer = Contract(45000, 'car') #make contracts
    Contract.print_contract(first_customer) #display contracts

    #what do we want to do?
    #have a buyer and seller -> probably need classes
    #contract class
    #marketplace -> bidding, buying and selling occur -> add and subtract contracts from here. 