import csv
import class_teacher

class ClassTeacherManager:
    def __init__(self):
        self.class_teachers = []

    def add_class_teacher(self, class_teacher):
        for teacher in self.class_teachers:
            if teacher.class_teacher_id == class_teacher.class_teacher_id:
                return False

        self.class_teachers.append(class_teacher)
        return True

    def remove_class_teacher(self, class_teacher_id):
        for teacher in self.class_teachers:
            if teacher.class_teacher_id == class_teacher_id:
                self.class_teachers.remove(teacher)
                return True

        return False

    def search_class_teacher(self, class_teacher_id):
        for teacher in self.class_teachers:
            if teacher.class_teacher_id == class_teacher_id:
                return teacher

        return None


    def view_class_teachers(self):
        return self.class_teachers

    def save_class_teacher(self):
        with open('class_teachers.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["class_teacher_id", "class_teacher_name"])

            for teacher in self.class_teachers:
                data = [
                    teacher.class_teacher_id,
                    teacher.class_teacher_name
                ]
                writer.writerow(data)

    def load_class_teachers(self):
        try:
            self.class_teachers.clear()

            with open('class_teachers.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)

                for row in reader:
                    class_teacher_id = int(row[0])
                    class_teacher_name = row[1]

                    self.class_teachers.append(
                        class_teacher.ClassTeacher(
                            class_teacher_id,
                            class_teacher_name
                        )
                    )

        except FileNotFoundError:
            pass