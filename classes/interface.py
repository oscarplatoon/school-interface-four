from os import sched_get_priority_max
from classes.school import School
from classes.staff import Staff


class SchoolInterface:

    def __init__(self,school_name):
        self.school = School(school_name)
        self.employee_logged_in = False


    def run(self):
        self.authenticate_user()
        while self.employee_logged_in == True:
            mode = input(self.menu())

            if mode == '1':
                self.school.list_students()
            elif mode == '2':
                student_id = input('Enter student id:')
                student_string = str(self.school.find_student_by_id(student_id))
                print(student_string)
            elif mode == '3':
                student_data = {'role': 'student'}
                student_data['name'] = input('Enter student name:\n')
                student_data['age'] = input('Enter student age: \n')
                student_data['school_id'] = input('Enter student school id: \n')
                student_data['password'] = input('Enter student password: \n')

                self.school.add_student(student_data)
            elif mode == '4':
                student_id = input("Please enter the student's id:\n")
                self.school.delete_student(student_id)
            elif mode == '5':
                break

    def menu(self):
        return "\nWhat would you like to do?\nOptions:\n1 list_students\n2 individul Student <student_id>\n3 add_student\n4 remove_student <student_id>\n5 quit\n"
    
    def authenticate_user(self):
        self.welcome = print(f"Welcome to {self.school} School\n________________________________")
        self.employee_login = self.welcome, input(f"\nPlease enter a valid employee ID: ")
        for staff in self.school.staff.employee_id:
            if self.staff == employee_login:
                return self.run()