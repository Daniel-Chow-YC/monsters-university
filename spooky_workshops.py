from student_monster_class import *

class SpookyWorkshops():

    def __init__(self, scary_subject, location, staff):
        self.scary_subject = scary_subject
        self.location = location
        self.staff = staff
        self.students_List = []

    def list_student_id(self):
        student_id_list = []
        for student in self.students_List:
            student_id_list.extend([student.uni_id])
        return student_id_list


    def add_students(self, list_of_student):
        self.students_List.extend(list_of_student)


# student_monster1 = StudentMonster('Mike', 1, 'A')
# student_monster2 = StudentMonster('James', 2, 'B')
# student_monster3 = StudentMonster('Jake', 3, 'B+')
# spooky1 = SpookyWorkshops('Maths', 'building B', 'Mr Jenkins')
# print('OG list:')
# spooky1.add_students([student_monster2, student_monster3])
# spooky1.list_student_id()
# print('New list:')
# spooky1.add_students([student_monster1])
# spooky1.list_student_id()



