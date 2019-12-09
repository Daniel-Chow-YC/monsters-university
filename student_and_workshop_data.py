from student_monster_class import *
from spooky_workshops import *
from lecture_theatre_class import *

student_monster1 = StudentMonster('Mike', '1', 'A')
student_monster2 = StudentMonster('James', '2', 'B')
student_monster3 = StudentMonster('Jake', '3', 'B+')
students_list = []
students_list.extend([student_monster1, student_monster2, student_monster3])

spooky_workshop1 = SpookyWorkshops('Maths', 'Building A', 'Mr Stevens')
spooky_workshop2 = SpookyWorkshops('Science', 'Building B', 'Mr Elroy')
spooky_workshop3 = SpookyWorkshops('English', 'Building C', 'Mr Jacobs')
running_workshops = []
running_workshops.extend([spooky_workshop1, spooky_workshop2, spooky_workshop3])