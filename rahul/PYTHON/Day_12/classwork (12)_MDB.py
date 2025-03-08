import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["doss"]
 
mycol = mydb["customers"]
query = {"address": {"$regex":"^S"}}

x = mycol.find(query)

for i in x:
    print(i)