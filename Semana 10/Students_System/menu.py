

def menu():
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

def user_option():
        return int(input('Input: '))

def get_valid_grade(subject,manager):
        while True:
            try:
                grade = int(input(f'{subject} Grade: '))
                return grade
            except ValueError:
                manager.clear_console()
                print("Invalid input. Please enter a numeric value.")

def ask_student_information(manager):
    while True:
        try:
            name = input('Add your Full Name: ')
            if not name.replace(" ", "").isalpha():
                raise ValueError('Name must contain letters only.')
            break
        except ValueError as e:
            manager.clear_console()
            print(f"Invalid input: {e}")

    group = input('Group: ')

    spanish_grade = get_valid_grade('Spanish',manager)
    english_grade = get_valid_grade('English',manager)
    social_grade = get_valid_grade('Social Studies',manager)
    science_grade = get_valid_grade('Science',manager)

    return {
        "name": name,
        "group": group,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_grade": social_grade,
        "science_grade": science_grade
    }



def add_another_student():
    return input('Would you like to add another Student: [Yes] or [No] ').strip().lower()

def students_format(aux):
    print("===================================")
    print(f" Full Name:       {aux['name']}")
    print(f" Group:           {aux['group']}")
    print(f" Spanish:         {aux['spanish_grade']}")
    print(f" English:         {aux['english_grade']}")
    print(f" Social Studies : {aux['social_grade']}")
    print(f" Science :        {aux['science_grade']}")
    print("===================================\n")

def back_option(manager):
    try:
         op = input('Would you like to come back to the Menu: [Yes] or [No] ').strip().lower()
         if not op.replace(" ","").isalpha():
              raise ValueError('Option must contain letter only')
         return op
    except ValueError as e:
         manager.clear_console()
         print(f'Input {e}')
         return None

def invalid_nof():
    print('Invalid Option')

def list_tittle():
    print('============ Student List ==========')


def av_gd_tittle():
    print('============ Student List ==========')