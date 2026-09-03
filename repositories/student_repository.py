import database

class StudentRepository:
    def __init__(self, database):
        self.database = database

    def add_student(self, student):
        try:
            cursor = self.database.cursor()
            

    def remove_student(self, student_id):
        pass

    def search_student(self, student_id):
        pass

    def view_students(self):
        pass