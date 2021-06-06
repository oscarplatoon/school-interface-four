# interface.py

from classes.school import School

class SchoolInterface:

    def __init__(self, school_name):
        self.school = School(school_name)
    
    def menu(self):
        return("\n"
            "What would you like to do?\n"
            "Options:\n"
            "1. List All Students\n"
            "2. View Individual Student <student_id>\n"
            "3. Add a Student\n"
            "4. Remove a Student <student_id>\n"
            "5. Quit\n")

    def list_all_students(self):
        return 0


    def run(self):
        while True:
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
