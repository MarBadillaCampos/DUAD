from menu import menu, user_option, ask_student_information, add_another_student,back_option
from actions import clear_console, add_students,read_Students_list 

def main():
    while True:
        menu()
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
            case 2:
                 clear_console()
                 print('======================================')
                 print('=============Student List=============')
                 read_Students_list()
                 bk_opt= back_option()
                 if bk_opt == 'yes':
                     continue
                 elif bk_opt == 'no':
                     break
                 else:
                        print('Invalid option')
            case 3:
                print('Este es el caso 3')
            case _:
                print("Invalid option")

if __name__ == '__main__':
    main()
