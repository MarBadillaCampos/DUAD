
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
        print("║  4.  view overall average grade      ║")
        print("║  5.  Delete Student                  ║")
        print("║  6.  Import Data                     ║")
        print("║  7.  Export Data                     ║")
        print("║  8.    extra                         ║")
        print("║  9.  Exit                            ║")
        print("╚══════════════════════════════════════╝")
    
    def ask_name(self):
        name = input('Add your name: ')
        return name
    
    def ask_group(self):
        group = input('Add your group:')
        return group
    
    def ask_spanish_score(self):
        spanish_score = int(input('Add your Spanish Score: '))
        return spanish_score
    
    def ask_english_score(self):
        english_score = int(input('Add your English Score: '))
        return english_score
    
    def ask_social_score(self):
        social_score = int(input('Add your Social Estudies Score: '))
        return social_score
    
    def ask_science_score(self):
        science_score = int(input('Add your science Score: '))
        return science_score
    
    def user_option(self):
        option = int(input('Input: '))
        return option
    
    def add_other_student(self):
        other_student = input('Do you want to add another Student [yes] or [no]: ')
        return other_student
    
    def confirm_action(self):
        confirm_ac = input('Confirm that you really want to remove this student: [yes] or [no]')
        return confirm_ac
    
    def delete_name(self):
        while True:
            try:
                name = input('Add the name that you would like to drop off: ')
                if not name.replace(" ", "").isalpha():
                    raise ValueError('Name must contain letters only. Please, try again!')
                return name
            except ValueError as e:
                print(f"Invalid input: {e}")
    
