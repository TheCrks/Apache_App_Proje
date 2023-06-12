from confluent_kafka import Producer
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import time
import json

global db, previous_db, client

# Apache Kafka Setup
bootstrap_servers = ""
while bootstrap_servers == "":
    bootstrap_servers = input("Enter bootstrap servers (eg. localhost:9092)")

topic = ""
while topic == "":
    topic = input("Enter Topic (eg. my_topic)")


# Method to send messages
def sendMessage(filename, server, topic):
    global db

    export_db_to_json(db, "db.json")

    producer = Producer({'bootstrap.servers': server})

    with open(filename, "r") as json_file:
        message = json_file.readlines()

    json_message = json.dumps(message)

    producer.produce(topic, json_message)

    producer.flush()


# Method to receive database
def getDb():
    global db, previous_db, client
    uri = "mongodb+srv://uuzun:EwuvFhEZNKySGgBE@cluster0.khd9rlb.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        db = client["sample_db_project"]
    except Exception as e:
        print(e)


getDb()
previous_db = []
previous_collections = ""


# Method to assign previous_db
def previous(filename):
    global db, previous_db, previous_collections
    export_db_to_json(db, "db.json")
    with open(filename, "r") as json_file:
        previous_db = json_file.readlines()
    previous_collections = db.list_collection_names()
    previous_db = [line.strip() for line in previous_db]


# Method to export database to a json file
def export_db_to_json(db, filename):
    open(filename, "w")
    # Fetch all documents from the specified collection
    collections = db.list_collection_names()
    document = []
    for x in collections:
        col = db[x]
        doc = col.find()
        document.append(doc)
    # Write the documents to a JSON file

    with open(filename, "a") as json_file:
        for doc in document:
            for y in doc:
                serialized_document = str(y)
                json_file.write(serialized_document + "\n")


export_db_to_json(db, "db.json")
previous("db.json")


# Method to compare current and previous databases
def compareDB():
    global previous_db, db, previous_collections
    string = []
    result = 1
    collections = db.list_collection_names()
    j = 0
    for x in collections:
        # if previous_collections gets out of bound there is most likely a new collection
        try:
            if x != previous_collections[j]:
                result += 1
        except Exception as e:
            print(e)
            print("Error Possible new collection. Returning -1")
            return -1
        j += 1
        collection = db[x]
        document = collection.find()
        for y in document:
            string.append(str(y))

    i = 0

    for s in string:
        # if previous_db gets out of bound there is most likely a new document
        try:
            if s != previous_db[i]:
                print(s + " != " + previous_db[i])
                result += 1
        except Exception as e:
            print(e)
            print("Error Possible new document. Returning -1")
            return -1
        i += 1
    return result


# Check if database is changed every 10 seconds
while 1:
    # If database is changed send message to kafka topic
    if compareDB() != 1:
        print("Database Changed")
        sendMessage("db.json", bootstrap_servers, topic)
    else:
        print("No changes")
    previous("db.json")
    time.sleep(10)
