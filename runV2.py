from spooky_workshops import *
from student_monster_class import *
from lecture_theatre_class import *
from student_and_workshop_data import *

while True:
    print('Choose an option:')
    print('1 -- Create a monster')
    print('2 -- List all workshops')
    print('3 -- Add student to spooky workshop')
    print('4 -- See students grade')
    print('5 -- Print a students full information from their Student ID')
    print('6 -- Print a students full information from their name')
    ui = input('Please choose a number or exit: ')
    if ui == '1':
        print('You have chosen option 1')
        name = input("What is the students name?")
        id = input("What is the students university ID?")
        grade = input('What is the students current grade?')
        new_student = StudentMonster(name, id, grade)
        students_list.extend([new_student])
        # print(students_list)

    elif ui == '2':
        print('You have chosen option 2')
        for spooky_workshop in running_workshops:
            print(spooky_workshop.scary_subject)

    elif ui == '3':
        print('You have chosen option 3')
        workshop = input('Select a workshop to add a student to. Select by subject: ')
        student = input('Select the student you wish to add to this workshop. Select by student ID ')
        for stu in students_list:
            if student == stu.uni_id:
                student_chosen = stu
                for spooky_workshop in running_workshops:
                    if workshop == spooky_workshop.scary_subject:
                        spooky_workshop.add_students([student_chosen])
                        print(spooky_workshop.list_student_id())

    elif ui == '4':
        print('You have chosen option 4')
        stu_id = input('Please input the students ID: ')
        for student in students_list:
            if stu_id == student.uni_id:
                print(student.get_grade())

    elif ui == '5':
        print('You have chosen option 5')
        stu_id = input('Please input the students ID: ')
        for student in students_list:
            if stu_id == student.uni_id:
                print(f"Name: {student.name}")
                print(f"Uni ID: {student.uni_id}")
                print(f"Grade: {student.get_grade()}")

    elif ui == '6':
        print('You have chosen option 6')
        stu_name = input('Please tell us the students name: ')
        for student in students_list:
            if stu_name == student.name:
                print(f"Name: {student.name}")
                print(f"Uni ID: {student.uni_id}")
                print(f"Grade: {student.get_grade()}")

    elif ui == 'exit':
        break

# ask for info
# evaluate info
# say which option you chose
# create a monster --1
# list all workshops --2
# add student to spooky workshop --3
# see students grade --4
# print full information of student --5
# search for student by name --6