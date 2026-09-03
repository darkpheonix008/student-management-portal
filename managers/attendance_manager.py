import csv
from models import attendance


class AttendanceManager:
    def __init__(self):
        self.attendance_records = []

    def add_attendance(self, attend):
        for atd in self.attendance_records:
            if atd.student_id == attend.student_id and atd.date == attend.date:
                return False
        else:
            self.attendance_records.append(attend)
            return True

    def remove_attendance(self, student_id, date):
        for atd in self.attendance_records:
            if atd.student_id == student_id and atd.date == date:
                self.attendance_records.remove(atd)
                return True
        else:
            return False

    def search_attendance(self, student_id, date):
        for atd in self.attendance_records:
            if atd.student_id == student_id and atd.date == date:
                return atd

        else:
            return None

    def view_attendance(self):
        return self.attendance_records

    def save_attendance(self):
        with open('../attendance.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["student_id", "date", "status"])
            for rec in self.attendance_records:
                data = [rec.student_id, rec.date, rec.status]
                writer.writerow(data)

    def load_attendance(self):
        try:
            self.attendance_records.clear()
            with open('../attendance.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                        student_id = int(row[0])
                        date = row[1]
                        status = row[2]
                        self.attendance_records.append(attendance.Attendance(student_id, date, status))
        except FileNotFoundError:
            pass

    def view_attendance_by_student(self, student_id):
        result = []
        for rec in self.attendance_records:
            if rec.student_id == student_id:
                result.append(rec)

        return result

    def calculate_attendance_percentage(self, student_id):
        attendance_earned = 0
        working_days = 0
        attendance_records = self.view_attendance_by_student(student_id)
        for rec in attendance_records:
            if rec.status.lower() != "holiday":
                working_days += 1
                if rec.status.lower() == "present":
                    attendance_earned += 1

                elif rec.status.lower() == "half-day":
                    attendance_earned += 0.5
        if working_days == 0:
            percentage = 0

        else:
            percentage = attendance_earned / working_days * 100

        return percentage
    def view_attendance_summary(self, student_id):
        present = absent = half_day = holiday = 0
        attendance_records = self.view_attendance_by_student(student_id)
        for rec in attendance_records:
            if rec.status.lower() == "present":
                present += 1
            elif rec.status.lower() == "absent":
                absent += 1
            elif rec.status.lower() == "half-day":
                half_day += 1
            elif rec.status.lower() == "holiday":
                holiday += 1
        percentage = self.calculate_attendance_percentage(student_id)
        return [present, absent, half_day, holiday, percentage]

    def student_has_attendance(self, student_id):
        for record in self.attendance_records:
            if record.student_id == student_id:
                return True
        return False




