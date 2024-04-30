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
         #myquery = { "name": Contract.name} #look for the contract we are adding within the database

         #need to find a way to get the contract_id 

         #mydoc = mycol.find(myquery)
         
         myquery = {"name": Contract.name}
         mydoc = mycol.find_one(myquery)
         print(mydoc.get('_id'), "of ID 2")

         print("Trying to print the count starting here")
         count =  list(mycol.find())
         print(len(count))
         for what in count:
            print(what)

         

         myquery2 = {"_id": len(count)}
         mydoc2 = mycol.find_one(myquery2)
         print(mydoc2.get('_id'), "of max ID")
         #working here

         #still need to find a way to reuse a contract_id if it is already in the system. 
         mydoc4 = list(mycol.find().sort( {"_id": -1}).limit(1))
         #this is storing the document I want from the database into 1 list item, not key value pairs. 

         mydoc5 = mycol.find().sort( {"_id": -1}).limit(1)
         print(mydoc5.get('_id'))

         #start here 
         #we have the max documents in the collection now -> so we can iterate that. 
         #maybe do a find name of contract then copy contract ID otherwise assign random number?
         



         #start here***    https://www.youtube.com/watch?v=UpsZDGutpZc
         #find the max _id and add one for the newest record.
         #if the contract name already exists, then find the contract_id for it already in the DB and use it
         #may need to do some conditional functions to accomplish this.
         
      

         #mydoc2 = mycol.find().sort( {"_id": -1}).limit(1)
         # for post in mydoc2:
         #    print(post)

         
         #we got the top ID from this... but need to extract the id value. 
         

         # for x in mydoc:
         #    print(x)
         # record = {
         #       "_id": 2,   #grab max Id and add 1 (+1)
         #       "contract_id": 2, #grab max contract_id and add 1 (+1)
         #       "name": Contract.name,
         #       "price": Contract.price,
         #       "time_inserted": datetime.datetime.now(),
         #       "status": "available"
         #       }
         # x = mycol.insert_one(record)

         #print(x.inserted_id) 
         #print("Successfully inserted into database with this id: " + str(x.inserted_id))
         #if the insert does not work, user will be notified 
      except Exception as error:
         print("Unsuccessfully inserted into MongoDB" + "Error is    ", error)
      



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
      