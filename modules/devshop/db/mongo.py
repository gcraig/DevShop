#!/usr/bin/env python
# -*- coding: utf-8 -*-

# automate?
# dependencies:
# 1. install python 3.3
# 2. pip install pymongo (as admin) or easy_install pymongo
# 3. easy_install virtualenv
# 4. mkdir project; cd project; virtualenv venv
# 5. activate: venv\scripts\activate
# 6. pip install Flask

import pymongo
from pymongo import MongoClient

# generic driver, dao, should be layered by CollectionDao
# i.e., ClientsDao, entity service with find/crud methods

class Mongo:

    def __init__(self):
        print("<<< Mongo db driver initialized >>>")        

    def getDatabase(self, databasename):
        return driver[databasename]

    def getCollection(self, databasename, collection):
        driver = MongoClient('WALTER', 27017)
        db = driver[databasename]
        collection = db[collection]
        return collection

    #
    # /////////////////////////////////////////////////////
    #
    
    def test(self):
        print("Example MongoDB client >>>")        
        client = MongoClient('WALTER', 27017)
        #client = MongoClient()
        #client = MongoClient('localhost', 27017)
        #client = MongoClient('mongodb://localhost:27017')

        print("Getting database 'local':")
        #db = client['local'] or
        db = client.local

        print("Getting 'Clients' collection:")
        Clients = db.Clients
        #print(Clients)

        #
        # find one
        #
        '''
        c = Clients.find_one()
        client_id = c['_id']
        client = c['name']
        print()
        print("client:", client)
        print("client_id:", client_id)
        #print(str(client_id).upper())
        '''

        #
        # insert one/many
        #

        #
        # find()   limit()
        #
        clients = Clients.find() #.limit(10)
        for client in clients:
            c_id = client['_id']
            c_name = client['name']
            print()
            print("client:", c_name)
            print("client_id:", c_id)

        #
        # update()
        #
        
        #
        # delete()
        #

        '''
        print("Iterating over each post(document in 'Clients' and printing:")
        for c in Clients.find():
            print(c)
        '''

        #system.indexes
