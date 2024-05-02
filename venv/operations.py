import datetime
import os
#import threading : may look into multithread to get the DB to load in the background

from contract import Contract
from seller import Seller
from buyer import Buyer

from dotenv import load_dotenv
from pymongo import MongoClient

class DB:
   def __init__(self, name):
      self.name = name

      # Load config from a .env file:
      load_dotenv()
      MONGODB_URI = os.environ['MONGODB_URI']
      
      # Connect to your MongoDB cluster:
      client = MongoClient(MONGODB_URI)
      self.connection = client


   def establish_connection(self):  
      # List all the databases in the cluster:
      for db_info in self.connection.list_database_names():
         print(db_info)

   @staticmethod
   def DB_insert_contract(self,Contract):
      print("Here is the contract {} at {}".format(Contract.name, Contract.price))
      #here we are capturing the contract name and price
      #Here are the elements I want to attach to the database entre along with these items:
            #ID, name, price, load date(date contract was added), status (sold or available) 
      try:
         #here we will have to grab the last items _id to interate for the next insertion
         #we wiill also havet to grab the last contract name and contract ID to either use the same contract_id or to interate a new one.
         mydb = self.connection["marketPlace_DB"]
         mycol = mydb["contracts"]

         #still need to find a way to reuse a contract_id if it is already in the system. 
         #mydoc4 = list(mycol.find().sort( {"_id": -1}).limit(1))
         #this is storing the document I want from the database into 1 list item, not key value pairs. 
         
         count =  list(mycol.find())
            #count will get the total amount of documents in the collection
         new_id = len(count)+1
            #amount of documents in the collection and add 1 to iterate a new _id for the new contract
                  # for x in mydoc:
                  #    print(x)
         record = {
               "_id": new_id,   #grab max Id and add 1 (+1)
               "contract_id": new_id, #grab max contract_id and add 1 (+1)
               "name": Contract.name,
               "price": Contract.price,
               "time_inserted": datetime.datetime.now(),
               "status": Contract.status
               }
         x = mycol.insert_one(record)

         print(x.inserted_id) 
         print("Successfully inserted into database with this id: " + str(x.inserted_id))
         #if the insert does not work, user will be notified 
      except Exception as error:
         print("Unsuccessfully inserted into MongoDB" + "Error is    ", error)
      
   def DB_trade_facilitor(self, Contract, Buyer, Seller):
      try:
            #add contracts to Buyer collection
            #set status in contracts and seller collection
            #add sold datetimes to each collection
            mydb = self.connection["marketPlace_DB"]
            mycol = mydb["contracts"]
         
            myquery = {"name": Contract.name}
         
            soldtime = datetime.datetime.now()
            add_soldtime = {"$set": {"Sold_Datetime": soldtime}}
            mycol.update_one(myquery, add_soldtime)
            #adds the sold date time of the contract 

            mydoc = mycol.find({"name": Contract.name})
            for x in mydoc:
                print(x)
            #show that the status was updated on the contract

      except Exception as error:
            print("Unsuccessfully inserted into MongoDB" + "Error is    ", error)
         

   def DB_insert_Seller(self, Seller):
      mydb = self.connection["marketPlace_DB"]
      mycol = mydb["sellers"]

      count =  list(mycol.find())
      new_id = len(count)+1

      record = {
          "_id": new_id,
          "name": Seller.name,
          "rating": Seller.rating,
          "time_inserted": datetime.datetime.now(),
         }
      x = mycol.insert_one(record)

      print(x.inserted_id) 
      print("Successfully inserted into database with this id: " + str(x.inserted_id))


      try:

         #iterate through the list of contracts that the seller owns and insert their _ids/names 
         #think about how we want these contracts to look within the seller document
         for x in Seller.list:
            myquery = {"name": Seller.name}
            add_contract = {"$push": {"contracts_owned": 
                     {
                     "Contract_name": x.name,
                     "Contract_price": x.price,
                     "Contract_status": x.status
                     }
            }
            }
            mycol.update_one(myquery, add_contract)

      except Exception as error:
            print("Unsuccessfully inserted into MongoDB" + "Error is    ", error)


   def DB_insert_buyer(self, Buyer):
      mydb = self.connection["marketPlace_DB"]
      mycol = mydb["buyers"]

      count =  list(mycol.find())
      new_id = len(count)+1

      record = {
          "_id": new_id,
          "name": Buyer.name,
          "rating": Buyer.rating
         }
   
      x = mycol.insert_one(record)

      print(x.inserted_id) 
      print("Successfully inserted into database with this id: " + str(x.inserted_id))
      