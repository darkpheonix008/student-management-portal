from models import attendance, class_teacher, classroom, student
import database
from managers import attendance_manager as atd_manager, class_teacher_manager as ct_manager, \
    classroom_manager as cr_manager, student_manager as std_manager

student_manager = std_manager.StudentManager()
attendance_manager = atd_manager.AttendanceManager()
classroom_manager = cr_manager.ClassroomManager()
class_teacher_manager = ct_manager.ClassTeacherManager()
db = database.Database('localhost', 'root', '6465', "student_management_system")
if db.connect():
    print('Database connected')
else:
    print('Database not connected')
def get_valid_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print('Please enter a valid number')

print('welcome to student manager')

student_manager.load_students()
attendance_manager.load_attendance()
classroom_manager.load_classroom()
class_teacher_manager.load_class_teachers()

def student_management(db):
    while True:
        print('''
        1.Add student
        2.Remove student
        3.Search students
        4.View students
        5.Back
        ''')

        choice2 = get_valid_input('Enter your choice(1/2/3/4/5): ')

        if choice2 == 1:
            std_id = get_valid_input('Enter student id: ')
            std_name = input('Enter student name: ')
            date_of_birth = input('Enter student date of birth: ')
            classroom_id = input('Enter student class id: ')

            result = classroom_manager.search_classroom(classroom_id)

            if result:
                std = student.Student(std_id, std_name, date_of_birth, classroom_id)
                if student_manager.add_student(std):
                    print(f'Student with id {std_id} added successfully')
                else:
                    print(f'Student with id {std_id} already exists')
            else:
                print(f'Classroom with id {classroom_id} not found')
        elif choice2 == 2:
            std_id = get_valid_input('Enter student id to remove student: ')

            if attendance_manager.student_has_attendance(std_id):
                print(f'Cannot remove student {std_id}. Attendance records exist.')
            else:
                if student_manager.remove_student(std_id):
                    print(f'Student with id {std_id} was removed')
                else:
                    print(f'Student with id {std_id} was not found')

        elif choice2 == 3:
            std_id = get_valid_input('Enter student id to search student: ')

            result = student_manager.search_student(std_id)

            if result:
                print(result)
            else:
                print(f'Student with id {std_id} not found')

        elif choice2 == 4:
            result = student_manager.view_students()

            if result:
                for student_record in result:
                    print(student_record)
            else:
                print('No records found')

        elif choice2 == 5:
            break

        else:
            print('Invalid choice')

def attendance_management():
    while True:
        print('''
               ATTENDANCE MANAGEMENT
               -----------------------
               1.Add attendance
               2.Remove attendance
               3.Search Attendance
               4.View attendance
               5.view attendance by student
               6.view student attendance percentage
               7.view student summary
               8.back
               ''')

        choice2 = get_valid_input('Enter your choice(1/2/3/4/5/6/7/8): ')

        if choice2 == 1:
            std_id = get_valid_input('Enter student id to add attendance: ')

            student_record = student_manager.search_student(std_id)

            if student_record:
                date = input('Enter attendance date(dd/mm/yyyy): ')
                status = input('Enter attendance status(Present/Absent/Half-day/Holiday): ')

                atd = attendance.Attendance(std_id, date, status)

                if attendance_manager.add_attendance(atd):
                    print(f'Attendance on {date} for id {std_id} added successfully')
                else:
                    print(f'Attendance on {date} for id {std_id} already exists')
            else:
                print(f'Student with id {std_id} not found')

        elif choice2 == 2:
            std_id = get_valid_input('Enter student id to remove attendance: ')
            date = input('Enter attendance date(dd/mm/yyyy): ')

            if attendance_manager.remove_attendance(std_id, date):
                print(f'Attendance on {date} for id {std_id} removed successfully')
            else:
                print(f'Attendance on {date} for id {std_id} not found')

        elif choice2 == 3:
            std_id = get_valid_input('Enter student id to search attendance: ')
            date = input('Enter attendance date to search(dd/mm/yyyy): ')

            result = attendance_manager.search_attendance(std_id, date)

            if result:
                print(result)
            else:
                print(f'Attendance on {date} for id {std_id} not found')

        elif choice2 == 4:
            result = attendance_manager.view_attendance()

            if result:
                for attendance_record in result:
                    print(attendance_record)
            else:
                print('No records found')

        elif choice2 == 5:
            search_student = get_valid_input('Enter student id to search student: ')
            result = attendance_manager.view_attendance_by_student(search_student)
            if result:
                for attendance_record in result:
                    print(attendance_record)
            else:
                print(f'no record found for student {search_student}')

        elif choice2 == 6:
            std_id = get_valid_input('Enter student id to display percentage: ')
            percentage = attendance_manager.calculate_attendance_percentage(std_id)
            print(f'The attendance percentage for student {std_id} is {percentage:.2f}%')

        elif choice2 == 7:
            student_id = get_valid_input('Enter student id to view student summary: ')
            present, absent, half_day, holiday, percentage = attendance_manager.view_attendance_summary(student_id)
            print(f'ATTENDANCE SUMMARY FOR STUDENT {student_id}\n'
                  f'--------------------------------------\n'
                  f'present    : {present}\n'
                  f'absent     : {absent}\n'
                  f'half-day   : {half_day}\n'
                  f'holiday    : {holiday}\n'
                  f'percentage : {percentage}%')

        elif choice2 == 8:
            break

        else:
            print('Invalid choice')

def classroom_management():
    while True:
        print('''
               CLASSROOM MANAGEMENT
               --------------------
               1.Add Classroom
               2.Remove Classroom
               3.Search Classroom
               4.View Classrooms
               5.Back
               ''')

        choice2 = get_valid_input('Enter your choice(1/2/3/4/5): ')

        if choice2 == 1:
            classroom_id = input('Enter classroom id (e.g. 10A): ')
            academic_year = input('Enter academic year: ')
            class_teacher_id = get_valid_input('Enter class teacher id: ')

            teacher = class_teacher_manager.search_class_teacher(class_teacher_id)

            if teacher:
                room = classroom.Classroom(
                    classroom_id,
                    academic_year,
                    class_teacher_id
                )

                if classroom_manager.add_classroom(room):
                    print(f'Classroom {classroom_id} added successfully')
                else:
                    print(f'Classroom {classroom_id} already exists')
            else:
                print(f'Teacher with id {class_teacher_id} not found')

        elif choice2 == 2:

            classroom_id = input('Enter classroom id to remove: ')

            if student_manager.students_in_classroom(classroom_id):

                print(f'Cannot remove classroom {classroom_id}. Students are still assigned to it.')

            else:

                if classroom_manager.remove_classroom(classroom_id):

                    print(f'Classroom {classroom_id} removed successfully')

                else:

                    print(f'Classroom {classroom_id} not found')

        elif choice2 == 3:
            classroom_id = input('Enter classroom id to search: ')

            result = classroom_manager.search_classroom(classroom_id)

            if result:
                print(result)
            else:
                print(f'Classroom {classroom_id} not found')

        elif choice2 == 4:
            result = classroom_manager.view_classrooms()

            if result:
                for room in result:
                    print(room)
            else:
                print('No classrooms found')

        elif choice2 == 5:
            break

        else:
            print('Invalid choice')

def class_teacher_management():
    while True:
        print('''
               CLASS TEACHER MANAGEMENT
               ------------------------
               1.Add Class Teacher
               2.Remove Class Teacher
               3.Search Class Teacher
               4.View Class Teachers
               5.Back
               ''')

        choice2 = get_valid_input('Enter your choice(1/2/3/4/5): ')

        if choice2 == 1:
            teacher_id = get_valid_input('Enter teacher id: ')
            teacher_name = input('Enter teacher name: ')

            teacher = class_teacher.ClassTeacher(
                teacher_id,
                teacher_name
            )

            if class_teacher_manager.add_class_teacher(teacher):
                print(f'Class teacher with id {teacher_id} added successfully')
            else:
                print(f'Class teacher with id {teacher_id} already exists')


        elif choice2 == 2:

            teacher_id = get_valid_input('Enter teacher id to remove: ')

            if classroom_manager.teacher_has_classroom(teacher_id):

                print(f'Cannot remove teacher {teacher_id}. They are assigned to a classroom.')

            else:

                if class_teacher_manager.remove_class_teacher(teacher_id):

                    print(f'Class teacher with id {teacher_id} removed successfully')

                else:

                    print(f'Class teacher with id {teacher_id} not found')

        elif choice2 == 3:
            teacher_id = get_valid_input('Enter teacher id to search: ')

            result = class_teacher_manager.search_class_teacher(teacher_id)

            if result:
                print(result)
            else:
                print(f'Class teacher with id {teacher_id} not found')

        elif choice2 == 4:
            result = class_teacher_manager.view_class_teachers()

            if result:
                for teacher in result:
                    print(teacher)
            else:
                print('No class teachers found')

        elif choice2 == 5:
            break

        else:
            print('Invalid choice')


while True:
    print('''
    STUDENT MANAGEMENT SYSTEM
    -------------------------
    1.Student management
    2.Attendance management
    3.Classroom management
    4.Class teacher management
    5.Exit
    ''')

    choice1 = get_valid_input('Enter your choice(1/2/3/4/5): ')

    if choice1 == 1:
        student_management()

    elif choice1 == 2:
       attendance_management()

    elif choice1 == 3:
       classroom_management()

    elif choice1 == 4:
       class_teacher_management()
    elif choice1 == 5:
        print('Closing Application')
        student_manager.save_students()
        attendance_manager.save_attendance()
        classroom_manager.save_classroom()
        class_teacher_manager.save_class_teacher()
        break

    else:
        print('Invalid choice')
