import pymongo

class Connection():
    def get_connection(self):
        try:
            connection = pymongo.MongoClient("mongodb://localhost:27017")
            database = connection["college"]
            return database
        except Exception as err:
            return err