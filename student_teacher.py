import pymongo

class ConnMgoSTClln:
    def connection(self):
        """
        created connection part
        :return: collection
        """
        connection = pymongo.MongoClient("mongodb://localhost:27017")
        database = connection["college"]
        print(database)
        collection = database['teacher_student_mapping']
        return collection

    def insert_record(self, data):
        """
        created function to insert documents in the collection
        :param data: data
        :return: document
        """
        collection = self.connection()
        document = collection.insert_one(data)
        return document


item = ConnMgoSTClln()
data = data={"_id":4,"stud_id":20,"teacher_id":11}
item.insert_record(data)
print(id)

