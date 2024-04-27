import datetime
import os
#import threading : may look into multithread to get the DB to load in the background

from contract import Contract

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
   def DB_insert_contract(Contract):
       print("Here is the contract {} at {}".format(Contract.get_name, Contract.get_price))




# if "marketPlace_DB" in client.list_database_names():
#    print("Database exists")
   
#    #add in logic to add new contract to existing database. 
# else:
#    #create new db by inserting document 
#    mydb = client["marketPlace_DB"]
#    mycol = mydb["contracts"]

#    first_contract = {"name": "Truck", "amount": "40,294"}   #this would come from the contract class
#    x = mycol.insert_one(first_contract)

#    print(x.inserted_id)    #ensure it was inserted
   

   #start here
      #DB is setup and working in mongoDB (json structure)
   #thoughts:
      #do we wan to have database insert methods by class or as a class of its own that is facilitated through main.
      