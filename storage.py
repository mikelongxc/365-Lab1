"""
Stores student data in four different relations

1. Key: Student Last Name
2. Key: Teacher Last Name
3. Key: Bus Route Number
4. Key: Grade Level
"""
class Student:
    def __init__(self, params):
        self.last_name = params[0]
        self.first_name = params[1]
        self.grade = params[2]
        self.classroom = params[3]
        self.bus = params[4]
        self.gpa = params[5]
        self.teacher_last_name = params[6]
        self.teacher_first_name = params[7]

    def print_student(self):
        print(f"{self.last_name}, {self.first_name}:\n\
            Grade: {self.grade},\n\
            Classroom: {self.classroom},\n\
            Bus: {self.bus},\n\
            GPA: {self.gpa},\n\
            Teacher: {self.teacher_last_name}, {self.teacher_first_name}\n"
        )

class Storage:
    students = {}
    teachers = {}
    busses = {}
    grades = {}

    def __init__(self, student_file):
        f = open(student_file, "r")
        lines = f.readlines()

        for line in lines:
            parsed_line = line.split(",")

            if len(parsed_line) != 8:
                print("ERROR: student data formatted incorrectly")
                exit(0)

            self.store_student(Student(parsed_line))

    def store_student(self, student):
        for key, storage in [
            (student.last_name, self.students), 
            (student.teacher_last_name, self.teachers),
            (student.bus, self.busses),
            (student.grade, self.grades)
            ]:
            if key in storage:
                storage[key].append(student)
            else:
                storage[key] = [student]

    def query(self, key, storage):
        return storage[key]
