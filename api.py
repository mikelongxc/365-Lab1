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

        self.parse_input(search_input)

    def parse_input(self, input):
        self.search_command = input.split()

        if self.search_command[0] not in SUPPORTED_COMMANDS:
            print(f"ERROR: invalid search command: {self.search_command[0]}\n")
            self.print_help()

        if self.search_command[0] in ("S", "Student"):
            self.student_search()
        elif self.search_command[0] in ("T", "Teacher"):
            self.teacher_search()
        elif self.search_command[0] in ("B", "Bus"):
            self.bus_search()
        elif self.search_command[0] in ("G", "Grade"):
            self.grade_search()
        elif self.search_command[0] in ("A", "Average"):
            self.average_search()
        elif self.search_command[0] in ("I", "Info"):
            self.print_help()
        elif self.search_command[0] in ("Q", "Quit"):
            exit(0)

    def student_search(self):
        students = self.storage.query(self.search_command[1], self.storage.students)

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
        students = self.storage.query(self.search_command[1], self.storage.teachers)

        print(f"Student[s] with teacher with last name {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                student.print_student()
        else:
            print("ERROR: invalid parameters for teacher search. (T[eacher] <lastname>\n")

    def bus_search(self):
        students = self.storage.query(self.search_command[1], self.storage.busses)

        print(f"Student[s] that take bus route {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                student.print_student()
        else:
            print("ERROR: invalid parameters for bus search. (B[us] <number>)\n")

    def grade_search(self):
        students = self.storage.query(self.search_command[1], self.storage.grades)

        print(f"Student[s] in grade level {self.search_command[1]}:\n")

        if len(self.search_command) == 2:
            for student in students:
                student.print_student()
        elif len(self.search_command) == 3 and self.search_command[2] in ("H", "High"):
            pass
        elif len(self.search_command) == 3 and self.search_command[2] in ("L", "Low"):
            pass
        else:
            print("ERROR: invalid parameters for grade search. (G[rade] <number> [H[igh]|L[ow]])\n")

    def average_search(self):
        students = self.storage.query(self.search_command[1], self.storage.grades)

        if len(self.search_command) == 2:
            print(f"Average GPA for grade {self.search_command[1]}: {self.avg_gpa(students)}\n")
        else:
            print("ERROR: invalid parameters for average search. (A[verage] <number>)")

    def max_gpa(self, students):
        pass

    def min_gpa(self, students):
        pass

    def avg_gpa(self, students):
        pass

        

