from monster_class import *

class StudentMonster(Monster):

    def __init__(self, name, uni_id, grade):
        super().__init__(name)
        self.uni_id = uni_id
        self.__grade = grade

    def get_grade(self):
        return f'{self.name}: {self.__grade}'

    # create a setter for the grade as well
    def set_grade(self, grade):
        self.__grade = grade

# example_student = StudentMonster('Jim', '001', 'A')
# example_student.add_skill(['scary'])
# print(example_student.skills)
# example_student.set_grade('B')
# print(example_student.get_grade())
