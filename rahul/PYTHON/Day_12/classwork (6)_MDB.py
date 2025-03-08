import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
 
mydb = myclient["doss"]
 
mycol = mydb["customers"]
 
mydoc = mycol.find().sort("name",-1)

for x in mydoc:
  print(x)