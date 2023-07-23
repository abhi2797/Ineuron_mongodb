import pymongo
client = pymongo.MongoClient("mongodb+srv://meenaabhi2797:YDx0zLQJxHgCtX3i@cluster0.jviexdz.mongodb.net/")
db = client.test
print(db)

d = {
     " name" :"Abhishek ",
     "email" : "meenaabhi2797@gmail.com",
     "surname" : "Meena"
}
db1 =client['mongotest']
coll = db1['test']
coll.insert_one(d)