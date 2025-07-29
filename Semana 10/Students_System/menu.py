import re

class MenuHandler:

    def __init__(self):
        pass

    def menu(self):
        print("╔══════════════════════════════════════╗")
        print("║         STUDENT MANAGEMENT SYSTEM    ║")
        print("╠══════════════════════════════════════╣")
        print("║  1.  Add Students                    ║")
        print("║  2.  View all students               ║")
        print("║  3.  View top 3 by average grade     ║")
        print("║  4.  view overall average grade      ║")
        print("║  5.  Export data                     ║")
        print("║  6.  Import data                     ║")
        print("║  7.  Exit                            ║")
        print("╚══════════════════════════════════════╝")

    def user_option(self):
        return int(input('Input: '))

    def get_valid_grade(self,subject,manager):
        while True:
            try:
                grade = int(input(f'{subject} Grade: [0-100]: '))
                if 0 <= grade <= 100:
                    return grade
                else:
                    manager.clear_console()
                    print(f'Grade must be between 0 and 100. Please try again')
                    
            except ValueError:
                manager.clear_console()
                print("Invalid input. Please enter a numeric value. Please try again")

    def get_valid_group(self, manager):
     while True:
          try:
               group = input('Group: ').strip()
               if re.fullmatch(r'[A-Za-z0-9]+', group):
                return group
               else:
                manager.clear_console()
                print('Only letters and numbers are allowed, Please try again')

          except ValueError:
             manager.clear_console()
             print("Invalid input")

    def ask_student_information(self, manager):
        while True:
            try:
                name = input('Add your Full Name: ')
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                break

            except ValueError as e:
                manager.clear_console()
                print(f"Invalid input: {e}")

        group = self.get_valid_group(manager)

        spanish_grade = self.get_valid_grade('Spanish',manager)
        english_grade = self.get_valid_grade('English',manager)
        social_grade = self.get_valid_grade('Social Studies',manager)
        science_grade = self.get_valid_grade('Science',manager)

        return {
        "name": name,
        "group": group,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_grade": social_grade,
        "science_grade": science_grade
    }

    def add_another_student(self,manager):
        while True:
            try: 
                other_student= input('Would you like to add another Student: [Yes] or [No] ').strip().lower()

                if other_student in ('yes', 'no'):
                    return other_student
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                manager.clear_console()
                print(f'{e}')

    def students_format(self,aux):
        print("===================================")
        print(f" Full Name:       {aux['name']}")
        print(f" Group:           {aux['group']}")
        print(f" Spanish:         {aux['spanish_grade']}")
        print(f" English:         {aux['english_grade']}")
        print(f" Social Studies : {aux['social_grade']}")
        print(f" Science :        {aux['science_grade']}")
        print("===================================\n")

    def back_option(self,manager):
        while True:
            try: 
                op = input('Would you like to come back to the Menu: [Yes] or [No] ').strip().lower()

                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                manager.clear_console()
                print(f'{e}')

    def invalid_nof(self):
        print('Invalid Option')

    def list_tittle(self):
        print('====================================')
        print('============ Student List ==========')


