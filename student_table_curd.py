import pymongo

class ConnST:
    def connection(self):
        """
         created connection part
        :return: collection
        """
        connection = pymongo.MongoClient("mongodb://localhost:27017")
        database = connection["college"]
        print(database)
        collection = database['student']
        return collection

    def insert_record(self, data):
        """
        created function to insert student data
        :param data: passing data
        :return: document
        """
        collection = self.connection()
        document = collection.insert_one(data)
        return document

    def get_record(self, Name):
        """
         created functionn to get records
        :param Name: passing param Name
        :return:
        """
        collection = self.connection()
        data = collection.find_one({'Name':Name})
        return data

    def get_all_records(self):
        """
        created function to get all records
        :return: data
        """
        collection = self.connection()
        data = collection.find()
        return list(data)

    def update_records(self, _id, data):
        """
         created function to update fields with reference of id and data
        :param _id: param id
        :param data: data
        :return: data
        """
        collection = self.connection()
        data = collection.update_one({'_id': _id}, {"$set":data})
        return data

    def delete_records(self, Name):
        """
        created delete function with reference of name
        :param Name: passing parama name
        :return: data
        """
        collection = self.connection()
        data = collection.delete_many({"Name": Name})
        return data

if __name__ == "__main__":
    item = ConnST()
    item.connection()
    item.insert_record( {'_id': 29, 'Name': 'param', 'address': 'banglore'})
    item.update_records({2, 'rushi'})
    item.get_all_records()
    records = item.get_all_records()
    print(records)

    item.get_record()
    item.delete_records()
