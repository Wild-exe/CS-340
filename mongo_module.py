from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        username = 'aacuser'
        password = 'user'
        self.client = MongoClient('mongodb://%s:%s@localhost:39009/AAC' % (username, password))
        self.database = self.client['AAC']["animals"]

    def create(self, database_doc: dict) -> bool:
        """ C in CRUD """
        if database_doc is not None:
            inserted = self.database.insert_one(database_doc)
            # Returns true if the created ID is found in database.
            if self.database.find({"_id": ObjectId(f"{inserted.inserted_id}")}).count() > 0:
                return True
            return False
        else:
            raise Exception("Nothing to save, data parameter empty")

    def read(self, query: dict):
        """ R in CRUD """
        if query is not None:
            # Assigns results of mongoDB query to result_cursor
            result_cursor = self.database.find(query)
            if result_cursor.count() == 0:
                raise Exception("No results for query")
            else:
                return result_cursor
        else:
            raise Exception("Must provide a query parameter.")
