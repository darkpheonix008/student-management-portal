import mysql.connector as mysql

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        if self.connection :
            return True
        return False


    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
            return True
        return False

if __name__ == '__main__':
    database = Database('localhost', 'root', '6465', "student_management_system")
    database.connect()