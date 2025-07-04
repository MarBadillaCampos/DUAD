from menu import menu, user_option, ask_student_information, add_another_student, back_option
from actions import StudentManager 

def main():
    manager = StudentManager() 

    while True:
        menu()
        option = user_option()

        match option:
            case 1:
                manager.clear_console()
                new_student = ask_student_information()
                manager.add_student(new_student)
                manager.clear_console()

                while True:
                    other_student = add_another_student()
                    if other_student == 'yes':
                        manager.clear_console()
                        aux_student = ask_student_information()
                        manager.add_student(aux_student)
                        manager.clear_console()
                    elif other_student == 'no':
                        break
                    else:
                        print('Invalid option')

            case 2:
                manager.clear_console()
                print('======================================')
                print('=============Student List=============')
                manager.read_students_list()

                bk_opt = back_option()
                if bk_opt == 'yes':
                    continue
                elif bk_opt == 'no':
                    break
                else:
                    print('Invalid option')

            case 3:
                  manager.clear_console()
                  average_list = manager.grades_average()
                  print('========== Promedios de estudiantes ==========')
                  my_sorted_list = manager.sort_my_average_list(average_list)
                  manager.read_average_list(my_sorted_list)
            case _:
                print("Invalid option")

if __name__ == '__main__':
    main()
