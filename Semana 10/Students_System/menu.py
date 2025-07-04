
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


def ask_student_information():
    name = input('Add your Full Name: ')
    group = input('Group: ')
    spanish_grade = input('Spanish Grade:')
    english_grade = input('English Grade: ')
    social_grade = input('Social Studies Grade: ')
    science_grade = input('Science Grade: ')
    return {"name": name, "group": group, "spanish_grade": spanish_grade, "english_grade": english_grade, "social_grade": social_grade, "science_grade": science_grade}

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

def back_option():
    return input('Would you like to come back to the Menu: [Yes] or [No] ').strip().lower()