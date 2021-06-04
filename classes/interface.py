from classes.school import School

class SchoolInterface:

    def __init__(self, school_name):
        self.school = School(school_name)
        self.authenticated_user = False

    def run(self):
        
        if self.authenticate_user():
        
            while True:
                mode = input(self.menu())

                if mode == '1':
                    self.school.list_students()
                elif mode == '2':
                    self.view_student()
                elif mode == '3':
                    self.add_student()
                elif mode == '4':
                    self.delete_student()
                elif mode == '5':
                    self.authenticate_user()
                elif mode == '6':
                    break  
        
        return
        



    def menu(self):
        return "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"

    def view_student(self):
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

    def delete_student(self):
        student_id = input("Please enter the student's id:\n")
        self.school.delete_student(student_id)
    
    def authenticate_user(self):
        authentication_fail_attempts = 0

        while True:
            employee_id = input("Please enter your employee ID:\n")
            password = input("Please enter your password:\n")
            self.authenticated_user = self.school.check_id_and_password(employee_id, password)
            
            if (not self.authenticated_user):
                authentication_fail_attempts += 1
                
            if (authentication_fail_attempts >= 3):
                print("Maximum number of authentication attempts reached")
                return False
            
            elif self.authenticated_user:
                return True
           
                

        
