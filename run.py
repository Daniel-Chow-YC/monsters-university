from student_monster_class import *
from spooky_workshops import *
# Create 3 student monsters (assign a variable student1, student2...)
student_monster1 = StudentMonster('Mike', 1, 'A')
student_monster2 = StudentMonster('James', 2, 'B')
student_monster3 = StudentMonster('Jake', 3, 'B+')

# add these to an empty list
students_list = []
students_list.extend([student_monster1, student_monster2, student_monster3])

# create empty list for running workshops
running_workshops = []
# Create 3 spooky_workshops (also set to variable)
spooky_workshop1 = SpookyWorkshops('Maths', 'Building A', 'Mr Stevens')
spooky_workshop2 = SpookyWorkshops('Science', 'Building B', 'Mr Elroy')
spooky_workshop3 = SpookyWorkshops('English', 'Building C', 'Mr Jacobs')

# add each workshop to list_of_running_workshops (append)
running_workshops.extend([spooky_workshop1, spooky_workshop2, spooky_workshop3])

# iterate over the list of workshops and print it
for subject in running_workshops:
    print(subject.scary_subject)

#iterate over the student list
    # call method to should the grade of the student and print
for student in students_list:
    print(student.get_grade())

# for each workshop
    # call the method add_studdent and pass in the student id
spooky_workshop1.add_students([student_monster1])
spooky_workshop2.add_students([student_monster1, student_monster2])
spooky_workshop3.add_students([student_monster1, student_monster2, student_monster3])
spooky_workshop3.list_student_id()




