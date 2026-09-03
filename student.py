class Student:
    def __init__(self, student_id, student_name, date_of_birth, classroom_id):
        self.student_id = student_id
        self.student_name = student_name
        self.date_of_birth = date_of_birth
        self.classroom_id = classroom_id

    def __str__(self):
        return f'{self.student_id} {self.student_name} {self.date_of_birth} {self.classroom_id}'