

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
        name = input('Add your full name: ')
        return name
    
    def ask_spanish_score(self):
        spanish_score = int(input('Add your Spanish Score: '))
        return spanish_score
    
    def ask_english_score(self):
        english_score = int(input('Add your English Score: '))
        return english_score
    
    def ask_social_score(self):
        social_score = int(input('Add your Social Score: '))
        return social_score
    
    def ask_science_score(self):
        science_score = int(input('Ask for your Science Score: '))
        return science_score
      
    def user_option(self):
        return int(input('Input: '))
    
    def ask_for_another_student(self):
        return input('Do you want to add another student ? ')

       
    

   