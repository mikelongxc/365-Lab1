from storage import Storage

SUPPORTED_COMMANDS = ["S", "Student", "T", "Teacher", "B", "Bus", "G", "Grade", "A", "Average", "I", "Info", "Q", "Quit"]

class API:
    search_command = []

    def __init__(self, student_file):
        self.storage = Storage(student_file)

        print("Welcome to the student search API.\n")
        self.print_help()

    def print_help(self):
        print("""usage: <command>: [<options>]

    commands:
        S[tudent]:  <lastname> [B[us]]
        T[eacher]:  <lastname>
        B[us]:  <number>
        G[rade]:  <number> [H[igh]|L[ow]]
        A[verage]:  <number>
        I[nfo]
        Q[uit]
                """)

    def prompt(self):
        search_input = input("> ")

        return self.parse_input(search_input)

    def parse_input(self, input):
        self.search_command = input.split()

        command = self.search_command[0]
        if ":" in command:
            command = command[:-1]

        if command not in SUPPORTED_COMMANDS:
            print(f"ERROR: invalid search command: {command}\n")
            self.print_help()

        if command in ("S", "Student"):
            self.student_search()
        elif command in ("T", "Teacher"):
            self.teacher_search()
        elif command in ("B", "Bus"):
            self.bus_search()
        elif command in ("G", "Grade"):
            self.grade_search()
        elif command in ("A", "Average"):
            self.average_search()
        elif command in ("I", "Info"):
            self.print_help()
        elif command in ("Q", "Quit"):
            return 0
        
        return 1

    def student_search(self):
        if self.search_command[1] in self.storage.students:
            students = self.storage.query(self.search_command[1], self.storage.students)
        else:
            print(f"No students found with last name {self.search_command[1]}\n")
            return

        print(f"Student[s] with last name {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                print(f"{student.last_name}, {student.first_name}:\n\
                    Grade: {student.grade},\n\
                    Classroom: {student.classroom},\n\
                    Teacher: {student.teacher_last_name}, {student.teacher_first_name}\n"
                )

        elif len(self.search_command) == 3 and self.search_command[2] in ("B", "Bus"):
            for student in students:
                print(f"{student.last_name}, {student.first_name}: Bus {student.bus}")
        else:
            print("ERROR: invalid parameters for student search. (S[tudent] <lastname> [B[us]]\n")

    def teacher_search(self):
        if self.search_command[1] in self.storage.teachers:
            students = self.storage.query(self.search_command[1], self.storage.teachers)
        else:
            print(f"No students found with teacher with last name {self.search_command[1]}\n")
            return

        print(f"Student[s] with teacher with last name {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                student.print_student()
        else:
            print("ERROR: invalid parameters for teacher search. (T[eacher] <lastname>\n")

    def bus_search(self):
        if self.search_command[1] in self.storage.busses:
            students = self.storage.query(self.search_command[1], self.storage.busses)
        else:
            print(f"No students found for bus route {self.search_command[1]}.")
            return

        print(f"Student[s] that take bus route {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                student.print_student()
        else:
            print("ERROR: invalid parameters for bus search. (B[us] <number>)\n")

    def grade_search(self):
        if self.search_command[1] in self.storage.grades:
            students = self.storage.query(self.search_command[1], self.storage.grades)
        else:
            print(f"No students found for grade {self.search_command[1]}.")
            return

        print(f"Student[s] in grade level {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                student.print_student()
        elif len(self.search_command) == 3 and self.search_command[2] in ("H", "High"):
            self.max_gpa(students).print_student()
        elif len(self.search_command) == 3 and self.search_command[2] in ("L", "Low"):
            self.min_gpa(students).print_student()
        else:
            print("ERROR: invalid parameters for grade search. (G[rade] <number> [H[igh]|L[ow]])\n")

    def average_search(self):
        if self.search_command[1] in self.storage.grades:
            students = self.storage.query(self.search_command[1], self.storage.grades)
        else:
            print(f"No students found for grade {self.search_command[1]}.")
            return

        if len(self.search_command) == 2:
            print(f"Average GPA for grade {self.search_command[1]}: {self.avg_gpa(students)}\n")
        else:
            print("ERROR: invalid parameters for average search. (A[verage] <number>)")

    def max_gpa(self, students):
        student_with_max_gpa = None

        for student in students:
            if student_with_max_gpa is None or float(student.gpa) > float(student_with_max_gpa.gpa):
                student_with_max_gpa = student
            
        return student_with_max_gpa

    def min_gpa(self, students):
        student_with_min_gpa = None

        for student in students:
            if student_with_min_gpa is None or float(student.gpa) < float(student_with_min_gpa.gpa):
                student_with_min_gpa = student
            
        return student_with_min_gpa

    def avg_gpa(self, students):
        gpa_sum = 0

        for student in students:
            gpa_sum += float(student.gpa)

        return round(gpa_sum / len(students), 2)

        

