import csv
import classroom

class ClassroomManager:
    def __init__(self):
        self.classrooms = []

    def add_classroom(self, classroom):
        for rec in self.classrooms:
            if rec.classroom_id == classroom.classroom_id:
                return False
        self.classrooms.append(classroom)
        return True

    def remove_classroom(self, classroom_id):
        for rec in self.classrooms:
            if rec.classroom_id == classroom_id:
                self.classrooms.remove(rec)
                return True
        return False

    def search_classroom(self, classroom_id):
        for rec in self.classrooms:
            if rec.classroom_id == classroom_id:
                return rec
        return None


    def view_classrooms(self):
        return self.classrooms

    def save_classroom(self):
        with open('classroom.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["classroom_id","academic_year","class_teacher_id"])
            for rec in self.classrooms:
                data = [rec.classroom_id,rec.academic_year,rec.class_teacher_id]
                writer.writerow(data)

    def load_classroom(self):
        try:
            self.classrooms.clear()
            with open('classroom.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                        classroom_id = row[0]
                        academic_year = row[1]
                        teacher_id = row[2]
                        self.classrooms.append(classroom.Classroom(classroom_id, academic_year, teacher_id))
        except FileNotFoundError:
            pass

    def teacher_has_classroom(self, class_teacher_id):
        for rec in self.classrooms:
            if rec.class_teacher_id == class_teacher_id:
                return True
        return False