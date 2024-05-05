from contract import Contract
from seller import Seller
from buyer import Buyer
from operations import DB
import time 

class main:
    def __init__(self) -> None:
        pass
    

    #DB testing
    #contracts_db = DB('contracts_db')

    #add new contract
    farm_land = Contract(142000400, 'farm_land')
    equipment_lease = Contract(235899, 'Machinery')

    #pass contract information over to operations class
    #DB.DB_insert_contract(contracts_db, equipment_lease)
        #confirmed the insert contract is working -> need to add to the sell feature
    
    #update document (contract item in collection) if sold.
    #DB.DB_update_contract(contracts_db, equipment_lease)
        #confirmed working

    #add seller to seller database along with contracts
    # seller_db = DB('seller_db')

    # Jimmy = Seller("Jimmy", 1)
    # Jimmy.add_contract_s(Jimmy, farm_land)  
    #     #add farm_land contract to Jimmy
    # Jimmy.add_contract_s(Jimmy, equipment_lease)    
    #     #add equipment_lease contract to Jimmy
    # seller_db.DB_insert_Seller(Jimmy)   
        #insert Jimmy into Seller collections database and add his contracts
    #confirmed working

    #setup buyer collection 
    

    
    #confirmed working 


    #start here: operations: DB_trade_facilitor
    #Order of operations:
        #Buyer is added
            #Run DB_insert_buyer
        #Seller is added 
        #Contracts are added
            #Run DB_insert_contract
        #Seller takes ownership of contracts 
            #run DB_insert_Seller

    #if trade (buy/sell) takes place:
        #need to consider redunancy step (check contract names before inserting into database)
        #Use class method to "transfer" contracts to buyer
        #have database read in contracts of the buyer 
        #set the status of the contract in contract and seller collections along with classes 
            #*going to maintain the list of contracts in the seller class to keep record of all owned contracts over time 
    #trial 1
    
    
    #workingwith Phil (existing buyer)
    # Phil = Buyer('Phil', 1)

    #db_connection.DB_insert_buyer(Phil)

    #new seller
    # Frank = Seller('Frank', 1)
    
    #new contracts
    # pallets = Contract(24300, 'Wood_pallets')
    # metal = Contract(340222, 'Metal_beams')
    # scaffholding = Contract(28999, 'Scaffholding')

    #insert seller in db (with their contracts)
    # Seller.add_contract_s(Frank, pallets)
    # Seller.add_contract_s(Frank, metal)
    # Seller.add_contract_s(Frank, scaffholding)

    # db_connection.DB_insert_contract(db_connection, pallets)
    # db_connection.DB_insert_contract(db_connection, metal)
    # db_connection.DB_insert_contract(db_connection, scaffholding)

    # db_connection.DB_insert_Seller(Frank)

    #do a sale
    # Buyer.buy_contract(Phil, Frank, metal)
    # Seller.sell_contract(Frank, metal)  #not really needed
    # db_connection.DB_trade_facilitor(metal, Phil, Frank)

   
    #duplicate checking system

    #initiate database class
    db_connection = DB('db_connection1')



    Sam = Seller('Sam', 1)
    twenty_unit_complex = Contract(2300897, 'Twenty Unit Complex')
    Sam.add_contract_s(Sam, twenty_unit_complex)

    #db_connection.DB_insert_Seller(Sam)

    #db_connection.DB_insert_contract(db_connection, twenty_unit_complex)

    #db_connection.DB_insert_contract(db_connection, twenty_unit_complex)
   
    Dave = Buyer('Dave', 1)
    db_connection.DB_insert_buyer(Dave)
    Buyer.buy_contract(Dave, Sam, twenty_unit_complex)
    Sam.sell_contract(Sam, twenty_unit_complex)
    #db_connection.DB_trade_facilitor(twenty_unit_complex, Dave, Sam)
   

    def run_program():
        while True:
            print('welcome to ContractSwap! Please enter your name and role')
            username = input('Enter Name: ')
            role = input('Are you are a buyer or seller? ')
            
            if role == 'seller':
                time.sleep(3) #wait 3 seconds
                user_as_seller = Seller(username, 1)    #rating is not very important in this scenario
                print('You have been added as a Seller! ')
                time.sleep(2)
                counter = 0
                print('Please enter the name and amounts of the contracts you want to sell, then type "done". To start, type "go". ')

                while True:
                    user_adding_contracts = input('Add contract? (or "done" to finish): ')
                    
                    if user_adding_contracts == 'done':
                        time.sleep(1)
                        print('You have added all your contracts, lets see them all: ')
                        user_as_seller.print_seller_contracts()
                        break   
                        
                    user_contract_name = input('Contract name: ')
                    user_contract_amount = int(input('Contract amount: '))
                    user_contract = Contract(user_contract_amount, user_contract_name)
                    Seller.add_contract_s(user_as_seller, user_contract)     
                    counter = counter + 1
                    print('contracts added:  ' + str(counter))
                        
                        
                        
                break
                

            else:
                time.sleep(3)
                user_as_buyer = Buyer(username, 1)
                print('You have been added as a Buyer!')
                break       #this should stop the loop



    #run_program()


    #in testing we made sure all of our classess and methods were working 
    def testing():
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