import pymongo

class ConnMgoSTClln:
    def connection(self):
        """
        created connection part
        :return: collection
        """

        try:
            connection = pymongo.MongoClient("mongodb://localhost:27017")
            database = connection["college"]
            print(database)
            collection = database['teacher_student_mapping']
            print(collection)
        except Exception as err:
            return

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

