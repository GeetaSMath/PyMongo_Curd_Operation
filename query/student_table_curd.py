
class ConnST:
    def __init__(self):
        self.connection = self.Connection.get_connection()
        self.database = self.Connection.get_connection.connection()
    def connection(self):
        collection = self.database['student']
        return collection

    def insert_record(self, data):
        """
        created function to insert student data
        :param data: passing data
        :return: document
        """
        try:
            collection = self.connection()
            document = collection.insert_one(data)
            return document
            ConnMgo.commitTransaction()
        except Exception as err:
            return  err

    def get_record(self, Name):
        """
         created functionn to get records
        :param Name: passing param Name
        :return:
        """
        try:
            collection = self.connection()
            data = collection.find_one({'Name':Name})
            return data
            ConnMgo.commitTransaction()
        except Exception as err:
            return err

    def get_all_records(self):
        """
        created function to get all records
        :return: data
        """
        try:
            collection = self.connection()
            data = collection.find()
            return list(data)
            ConnMgo.commitTransaction()
        except Exception as err:
            return  err

    def update_records(self, _id, data):
        """
         created function to update fields with reference of id and data
        :param _id: param id
        :param data: data
        :return: data
        """
        try:
            print(_id, data)
            collection = self.connection()
            data = collection.update_one({'_id': _id}, {"$set":data})
            ConnST.commitTransaction()
            return data
        except Exception as err:
            return err

    def delete_records(self, Name):
        """
        created delete function with reference of name
        :param Name: passing parama name
        :return: data
        """
        try:
            collection = self.connection()
            data = collection.delete_many({"Name": Name})
            ConnST.commitTransaction()
            return data
        except Exception as err:
            return err

