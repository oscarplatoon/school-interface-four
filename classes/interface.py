from classes.school import School

class SchoolInterface:

    def __init__(self, school_name):
        self.school = School(school_name)
        self.authentication = False
        self.login_attempt = 0

    def authenticate_user(self):
        while self.authentication == False:
                login = input('Please enter a valid employee id:\n')
                password = input('Please enter a valid password:\n')
            
                for staff in self.school.staff:
                    if (staff.employee_id == login and staff.password == password):
                        self.authentication = True
                        break

                if self.authentication == True:
                    print(f'\nAccess Granted\n')
                    break
                elif self.login_attempt == 3:
                    print('Too many unsuccessful attempts')
                    input('System shutting down...')
                    quit()
                else:
                    self.login_attempt += 1
                    print('\nUsername/Password combination is incorrect.')
                    print(f'Unsuccesful attempt: {self.login_attempt} ///System will shut down on third unseccessful attempt.\n')

    def run(self):
        print(f'\n\nWelcome to {self.school.name}')
        print('________________________\n')

        while True:

            self.authenticate_user()

            mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

            if mode == '1':
                self.school.list_students()
            elif mode == '2':
                student_id = input('Enter student id:')
                student_string = str(self.school.find_student_by_id(student_id))
                print(student_string)
            elif mode == '3':
                student_data = {'role':'student'}
                student_data['name']      = input('Enter student name:\n')
                student_data['age']       = input('Enter student age: \n')
                student_data['school_id'] = input('Enter student school id: \n')
                student_data['password']  = input('Enter student password: \n')
                
                self.school.add_student(student_data)
            elif mode == '4':
                student_id = input("Please enter the student's id:\n")
                self.school.delete_student(student_id)
            elif mode == '5':
                break  