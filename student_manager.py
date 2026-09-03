import csv
import student
class StudentManager:
    def __init__(self,):
        self.students = []


    def add_student(self, stud):
        for std in self.students:
            if stud.student_id == std.student_id:
                return False

        else:
            self.students.append(stud)
            return True

    def remove_student(self, student_id):
        for std in self.students:
            if student_id == std.student_id:
                self.students.remove(std)
                return True
        else:
            return False

    def search_student(self, student_id):
        for std in self.students:
            if student_id == std.student_id:
                return std

        else:
            return None

    def view_students(self):
        return self.students

    def save_students(self):
        with open('students.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["student_id","student_name","date_of_birth", "classroom_id"])
            for std in self.students:
                data = [std.student_id,std.student_name,std.date_of_birth,std.classroom_id]
                writer.writerow(data)

    def load_students(self):
        try:
            self.students.clear()
            with open('students.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                        student_id = int(row[0])
                        student_name = row[1]
                        date_of_birth = row[2]
                        classroom_id = row[3]
                        self.students.append(student.Student(student_id, student_name, date_of_birth, classroom_id))
        except FileNotFoundError:
            pass

    def students_in_classroom(self, classroom_id):
        for std in self.students:
            if std.classroom_id == classroom_id:
                return True
        return False

