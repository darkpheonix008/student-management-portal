class ClassTeacher:
    def __init__(self, class_teacher_id, class_teacher_name):
        self.class_teacher_id = class_teacher_id
        self.class_teacher_name = class_teacher_name


    def __str__(self):
        return f'{self.class_teacher_id}, {self.class_teacher_name}'