from query.student_teacher import ConnMgoSTClln
from query.student_table_curd import ConnST
from query.teacher_table_curd import ConnMgo

class ControllCall():

    def get_student_info(self):
        item = ConnST()
        item.insert_record()
        output=item.get_record()
        for out in output:
            print(out)
        item.delete_records(),
        item.update_records()

    def get_teacher_info(self):
        item = ConnMgo()
        item.insert_record()
        output=item.get_record()
        for out in output:
            print(out)
        item.update_records(),
        item.delete_records()

    def get_stu_teacher_info(self):
        item = ConnMgoSTClln()
        item.insert_record()

    if __name__ == "__main__":
        while True:
            choice = int(input("enter your choice"))
            my_dict = {
                1:get_teacher_info,
                2:get_student_info,
                3:get_stu_teacher_info
            }
            my_dict.get(choice)()

