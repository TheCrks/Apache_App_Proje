from json import JSONEncoder

from pymongo import MongoClient
from pymongo.server_api import ServerApi
import time
import json

global db, previous_db, client


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
previous_db =[]


def previous(filename):
    global db, previous_db
    export_db_to_json(db, "db.json")
    with open(filename, "r") as json_file:
        previous_db = json_file.readlines()

    previous_db = [line.strip() for line in previous_db]


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


def compareDB():
    global previous_db, db
    string = []
    result = 1
    collections = db.list_collection_names()
    for x in collections:
        collection = db[x]
        document = collection.find()
        i = 0
        for y in document:
            string.append(str(y))

    i = 0

    for s in string:
        if s != previous_db[i]:
            print(s + " != " + previous_db[i])
            result += 1
        i+=1
    return result


while 1:
    if compareDB() != 1:
        print("Database Changed")
    else:
        print("No changes")
    previous("db.json")
    time.sleep(10)
