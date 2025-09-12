import re
class menuHandler:
    def __init__(self):
        pass

    def menu(self):
        print("╔══════════════════════════════════════╗")
        print("║         STUDENT MANAGEMENT SYSTEM    ║")
        print("╠══════════════════════════════════════╣")
        print("║  1.  Add Students                    ║")
        print("║  2.  View all students               ║")
        print("║  3.  View top 3 by average grade     ║")
        print("║  4.  View overall average grade      ║")
        print("║  5.  Delete Student                  ║")
        print("║  6.  Export Data                     ║")
        print("║  7.  Import Data                     ║")
        print("║  8.  View Failed Students            ║")
        print("║  9.  Exit                            ║")
        print("╚══════════════════════════════════════╝")
    
    def ask_name(self):
        while True:
            try:
                name = input('Add your name: ').strip().upper()
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
                
        return name
    
    def ask_group(self):
     while True:
          try:
               group = input('Group: ').strip()
               if re.fullmatch(r'[0-9]{2}[A-Z]{1}+', group):
                return group
               else:
                print('Invalid Format,it must be 2 number followed by an uppercase letter, Please try again')

          except ValueError:
             print("Invalid input")

    def ask_spanish_score(self):
        while True:
            try:
                spanish_score = int(input(f' Add your Spanish Grade [0-100]: '))
                if 0 <= spanish_score <= 100:
                    return spanish_score
                else:
                    print(f'Grade must be between 0 and 100. Please try again')
                    
            except ValueError:
                print("Invalid input. Please enter a numeric value. Please try again")
    
    def ask_english_score(self):
        while True:
            try:
                english_score = int(input(f' Add your English Score [0-100]: '))
                if 0 <= english_score <= 100:
                    return english_score
                else:
                    print(f'Grade must be between 0 and 100. Please try again')
                    
            except ValueError:
                print("Invalid input. Please enter a numeric value. Please try again")
    
    
    def ask_social_score(self):
        while True:
            try:
                social_score = int(input(f' Add your Social Estudies Score [0-100]: '))
                if 0 <= social_score <= 100:
                    return social_score
                else:
                    print(f'Grade must be between 0 and 100. Please try again')
                    
            except ValueError:
                print("Invalid input. Please enter a numeric value. Please try again")
    
    
    def ask_science_score(self):
        while True:
            try:
                science_score = int(input(f' Add your Science Grade [0-100]: '))
                if 0 <= science_score <= 100:
                    return science_score
                else:
                    print(f'Grade must be between 0 and 100. Please try again')
                    
            except ValueError:
                print("Invalid input. Please enter a numeric value. Please try again")
    
    def user_option(self):
        option = int(input('Input: '))
        return option
    
    def add_other_student(self):
        other_student = input('Do you want to add another Student [yes] or [no]: ')
        return other_student
    
    def confirm_action(self):
        while True:
            try: 
                confirm_ac = input('Confirm that you really want to remove this student: [yes] or [no]').strip().lower()

                if confirm_ac in ('yes', 'no'):
                    return confirm_ac
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')
    
    def ask_for_delete_name(self):
        while True:
            try:
                name = input('Add the name that you would like to delete: ').upper().strip()
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                return name
            except ValueError as e:
                print(f"Invalid input: {e}")


    def back_option(self):
        while True:
            try: 
                op = input('Would you like to come back to the Menu: [yes] or [no] ').strip().lower()

                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')
    
    def students_format(self,student):
        print("===================================")
        print(f" Full Name:       {student.name}")
        print(f" Group:           {student.group}")
        print(f" Spanish:         {student.spanish_score}")
        print(f" English:         {student.english_score}")
        print(f" Social Studies : {student.social_score}")
        print(f" Science :        {student.science_score}")
        print("===================================\n")
