class Classroom:
    def __init__(self,classroom_id, academic_year, class_teacher_id):
        self.classroom_id = classroom_id
        self.academic_year = academic_year
        self.class_teacher_id = class_teacher_id

    def __str__(self):
        return f'{self.classroom_id} {self.academic_year} {self.class_teacher_id}'



