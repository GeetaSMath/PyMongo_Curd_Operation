import pymongo
from connection import Connection

class ConnMgo:
    def __init__(self):
        self.connection = self.Connection.get_connection()
        self.database = self.Connection.get_connection.connection()

    def insert_record(self, data):
        """
         created insert function to pass param
        :param data: data
        :return: return document
        """
        try:
            collection = self.connection()
            document = collection.insert_one(data)
            print(document)
            ConnMgo.commitTransaction()
        except Exception as err:
            return err

    def get_record(self, Name):
        """
        created get function to  retrive data
        :param Name: passing parama Name
        :return: data
        """
        try:
            collection = self.connection()
            data = collection.find_one({"TeacherName":Name})
            print (data)
            ConnMgo.commitTransaction()
        except Exception as err:
            return err

    def get_all_records(self):
        """
        created function to get all records
        :return: data
        :return: data
        """
        try:
            collection = self.connection()
            data = collection.find()
            return list(data)
            ConnMgo.commitTransaction()
        except Exception as err:
            return err

    def update_records(self, _id, data):
        """
        created function update data which id existed with reference of qid and data
        :param _id: passing id
        :param data: data
        :return: data
        """
        try:

            collection = self.connection()
            data = collection.update_one({'_id': _id}, {"$set":data})
            print(data)
            ConnMgo.commitTransaction()
        except Exception as err:
            return err

    def delete_records(self, Name):
        """
         created function to delete data from the collectioon
        :param Name: passing param Name
        :return: data
        """
        try:
            collection = self.connection()
            data = collection.delete_many({"TeacherName": Name})
            print(data)
            ConnMgo.commitTransaction()

        except Exception as err:
            return err

