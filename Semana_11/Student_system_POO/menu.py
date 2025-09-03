import re

class MenuHandler:

    def __init__(self):
        pass

    def main_view(self):
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


    def ask_name(self):
        while True:
            try:
                name = input('Add your full name: ')
                if not name.replace(" ","").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
        return name
        

    
    def ask_group(self):
        while True:
            try: 
                group = input('Add your group value: ').strip()
                if re.fullmatch(r'[A-Za-z0-9]+', group):
                    return group
                else:
                    print('Only letters and numbers are allowed, Please try again')
            except ValueError:
             print("Invalid input")        
    

    def ask_spanish_score(self):
        while True:
            try:
                spanish_score = int(input('Add your Spanish Score: '))
                if 0 <= spanish_score <= 100:
                    return spanish_score
                else:
                    print('Grade must be between 0 and 100. Please try again')
            except ValueError:
                 print("Invalid input. Please enter a numeric value. Please try again")
    
    def ask_english_score(self):
        while True:
            try:
                english_score = int(input('Add your English Score: '))
                if 0 <= english_score <= 100: 
                    return english_score
                else:
                  print('Grade must be between 0 and 100. Please try again')  
            except ValueError:
                print('Invalid input. Please enter a numeric value. Please try again"')
    
    def ask_social_score(self):
        while True:
            try:
                social_score = int(input('Add your Social Score: '))
                if 0 <= social_score <= 100:
                    return social_score
                else:
                  print('Grade must be between 0 and 100. Please try again')
            except ValueError:
                print('Invalid input. Please enter a numeric value. Please try again"')
    
    def ask_science_score(self):
        while True:
            try:
                science_score = int(input('Add your Science Score: '))
                if 0 <= science_score <= 100:
                    return science_score
                else:
                  print('Grade must be between 0 and 100. Please try again')
            except ValueError:
                print('Invalid input. Please enter a numeric value. Please try again"')

      
    def user_option(self):
        return int(input('Input: '))
    
    def ask_for_another_student(self):
        return input('Do you want to add another student [yes] or [no]? ')
    
    def back_option(self):
        while True:
            try: 
                op = input('Would you like to come back to the Menu: [Yes] or [No] ').strip().lower()

                if op in ('yes', 'no'):
                    return op
                else:
                    raise ValueError ('Input must be [yes] or [no]')
            except ValueError as e:
                print(f'{e}')

       
    

   