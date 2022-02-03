import mongoengine

class Connection():
    def get_connection(self):
        """
         created function to make connection
        :return:
        """
        try:
            connection = mongoengine.MongoClient("mongodb://localhost:27017")
            database = connection["college"]
            return database
        except Exception as err:
            return err