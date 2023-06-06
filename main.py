from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
#def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb+srv://uuzun:<password>@cluster0.khd9rlb.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
#    return client['user_shopping_list']


# This is added so that many files can reuse the function get_database()
#if __name__ == "__main__":
    # Get the database
 #   dbname = get_database()
username = quote_plus('uuzun')
password = quote_plus('162Crks%2F*-123')
#cluster = '<clusterName>'
#authSource = '<authSource>'
#authMechanism = '<authMechanism>'
#uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism



uri = "mongodb+srv://uuzun:EwuvFhEZNKySGgBE@cluster0.khd9rlb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["sample_analytics"]
col = db["customers"]
doc = col.find()
for x in doc:
    print(x)
