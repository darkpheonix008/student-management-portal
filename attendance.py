
class Attendance:
    def __init__(self, student_id, date, status):
        self.student_id = student_id
        self.date = date
        self.status = status

    def __str__(self):
        return f'{self.student_id} {self.date} {self.status}'