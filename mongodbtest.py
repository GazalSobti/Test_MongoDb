import pymongo
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#print(db)
client = pymongo.MongoClient("mongodb+srv://gazalsobti:gazal2002@cluster0.tgt6jdx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name":"gazal",
   "email":"gazalsobti786@gmail.com",
   "surname":"sobti"}

db1=client['mongotest']
coll=db1['test']
call=db1['test']
call.insert_one(d)