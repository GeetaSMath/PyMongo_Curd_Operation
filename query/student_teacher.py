import pymongo

class ConnMgoSTClln:
    def __init__(self):
        self.connection = self.Connection.get_connection()
        self.database = self.Connection.get_connection.connection()

    def connection(self):
        try:
            collection = self.database['student']
            return collection
        except Exception as err:
            return err

    def insert_record(self, data):
        """
        created function to insert documents in the collection
        :param data: data
        :return: document
        """
        try:
            collection = self.connection()
            document = collection.insert_one(data)
            print(document)
        except Exception as err:
            return err


if __name__ == "__main__":
    item = ConnMgoSTClln()
    item.insert_record({"_id":6,"stud_id":22,"teacher_id":23})

