
import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo as pyM

uri = "mongodb+srv://pymongo:vfde2323@cluster0.gnysxhs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = pyM.MongoClient(uri)
db = client.test


clientes = [
    {
        "nome" : "joao",
        "cpf" : "123456789",
        "endereço" : "aabababa",
        'id' : 1,
    },
    {
        "nome" : "marcos",
        "cpf" : "134567898",
        "endereço" : "aabababa",
        'id' : 2,
    },
    {
        "nome" : "jorge",
        "cpf" : "098765432",
        "endereço" : "abububu",
        'id' : 3,
    }
   ]

posts = db.posts
# post_id = posts.insert_one(post).inserted_id

# print(post_id)
# print(db.list_collection_names())

#imprimir bonito


result = posts.insert_many(clientes)

print(result.inserted_ids)
pprint.pprint(db.posts.find_one())

for post in db.posts:
    print(post)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)