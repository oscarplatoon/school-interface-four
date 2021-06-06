from classes.school import School

class SchoolInterface:
  
    def __init__(self, school_name):
        self.school = School(school_name)
        self.auth_check = False

    def run(self):
        if self.authenticated_user():
            while True:
                mode = input(self.menu())

                if mode == '1':
                    self.school.list_students()
                elif mode == '2':
                    self.find_student()
                elif mode == '3':
                    self.add_student()
                elif mode == '4':
                    self.remove_student()
                elif mode == '5':
                    break  
    
    def menu(self):
        return "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"
        
    def find_student(self):
        student_id = input('Enter student id:')
        student_string = str(self.school.find_student_by_id(student_id))
        print(student_string)

    def add_student(self):
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')

        self.school.add_student(student_data)

    def remove_student(self):
        student_id = input("Please enter the student's id:\n")

        self.school.delete_student(student_id)

    def authenticated_user(self):
        auth_fail = 0

        while auth_fail < 3:

            staff_auth_id = input("\nEnter your employee id: ")
            staff_auth_pw = input("\nEnter your password: ")

            self.auth_check = self.school.check_employee_auth(staff_auth_id,staff_auth_pw)

            if not self.auth_check:
                auth_fail +=1
                
            else:
                return True
        
        print("You've failed authentification too many times")

        return False