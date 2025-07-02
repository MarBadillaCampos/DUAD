from menu import mostrar_menu, user_option, ask_student_information, add_another_student
from actions import clear_console, add_students, get_students_list

def main():
    while True:
        mostrar_menu()
        option = user_option()
        match option:
            case 1:
                clear_console()
                new_student = ask_student_information()
                add_students(new_student)
                clear_console()
                
                while True:
                    other_student = add_another_student()
                    if other_student == 'yes':
                        clear_console()
                        aux_student = ask_student_information()
                        add_students(aux_student)
                        clear_console()
                    elif other_student == 'no':
                        break  
                    else:
                        print('Invalid option')
                for student in get_students_list():
                    print(student)

            case 2:
                print('Este es el caso 2')
            case 3:
                print('Este es el caso 3')
            case _:
                print("Invalid option")

if __name__ == '__main__':
    main()
