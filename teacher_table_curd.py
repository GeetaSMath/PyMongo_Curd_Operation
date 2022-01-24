
import pymongo

class ConnMgo:
    def connection(self):
        """
         created function to create connectivity mongo to pymongo
        :return: collection
        """
        connection = pymongo.MongoClient("mongodb://localhost:27017")
        database = connection["college"]
        print(database)
        collection = database['faculty']
        return collection

    def insert_record(self, data):
        """
         created insert function to pass param
        :param data: data
        :return: return document
        """
        collection = self.connection()
        document = collection.insert_one(data)
        return document

    def get_record(self, Name):
        """
        created get function to  retrive data
        :param Name: passing parama Name
        :return: data
        """
        collection = self.connection()
        data = collection.find_one({"TeacherName":Name})
        return data

    def get_all_records(self):
        """
        created function to get all records
        :return: data
        :return: data
        """
        collection = self.connection()
        data = collection.find()
        return list(data)

    def update_records(self, _id, data):
        """
        created function update data which id existed with reference of qid and data
        :param _id: passing id
        :param data: data
        :return: data
        """
        collection = self.connection()
        data = collection.update_one({'_id': _id}, {"$set":data})
        return data

    def delete_records(self, Name):
        """
         created function to delete data from the collectioon
        :param Name: passing param Name
        :return: data
        """
        collection = self.connection()
        data = collection.delete_many({"TeacherName": Name})
        return data

if __name__ == "__main__":
    item = ConnMgo()
    item.connection()
    # item.insert_record({"_id": 502, "teacher_name": "pallavi", "department": {"dept_id": 10, "dept_Name": "civil"}})
    # item.update_records(2,{'TeacherName': 'aishu'})
    # item.delete_records('aishu')

    user_choice = int(input("Enter your choices "))
    mydict = {
                1:print(item.get_all_records()),
                2:print(item.get_record('laxmi'))
     }
    mydict.get(user_choice)

