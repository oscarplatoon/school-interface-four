from .school import School

class SchoolInterface:
    def __init__(self, school_name) -> None:
        self.school = School(school_name)
        self.logged_in = False
        self.user_name = ""
        self.password_error_count = 0

    def run(self):
        print(f"Welcome to {self.school.name}\n----------------------------")
        while self.logged_in == False:
            self.logged_in = self.authenticate_user()
            if self.logged_in == True:
                mode = input(self.menu())
                if mode == '1':
                    self.school.list_students()
                elif mode == '2':
                    student_id = input('Enter student id:')
                    student_string = str(
                        self.school.find_student_by_id(student_id))
                    print(student_string)
                elif mode == '3':
                    self.student_lookup()
                elif mode == '4':
                    student_id = input("Please enter the student's id:\n")
                    self.school.delete_student(student_id)
                elif mode == '5':
                    return
    
    def menu(self):
        return ("\nWhat would you like to do?\nOptions:\n1 list_students\n2 individul Student <student_id>\n3 add_student\n4 remove_student <student_id>\n5 quit\n")
    def student_lookup(self):
        student_data = {'role': 'student'}
        student_data['name'] = input('Enter student name:\n')
        student_data['age'] = input('Enter student age: \n')
        student_data['school_id'] = input(
            'Enter student school id: \n')
        student_data['password'] = input('Enter student password: \n')

        self.school.add_student(student_data)

    def authenticate_user(self):
        user_id = input("Please enter a valid employee ID: \n")
        for staff in self.school.staff:
            if staff.employee_id == user_id:
                while self.password_error_count < 3:
                    user_pass = input(f"Thanks {staff.name}, please enter your password:\n")
                    if staff.password == user_pass:
                        self.user_name = staff.name
                        print(f"Password accepted {staff.name}, thank you. Logging in...\n")
                        return True
                    else:
                        print("Incorrect password\n")
                        self.password_error_count += 1
                    
                print("You should ask your IT folks to reset your password.")
                return
        else:
            print("Incorrect User ID.\n")
            return False
