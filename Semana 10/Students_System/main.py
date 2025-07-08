from menu import menu, user_option, ask_student_information, add_another_student, back_option,invalid_nof,list_tittle,av_gd_tittle
from actions import StudentManager 

def main():
    manager = StudentManager() 

    while True:
        menu()
        try: 
            option = user_option()
            if 1 <= option <= 7:
                match option:
                    case 1:
                        manager.clear_console()
                        new_student = ask_student_information(manager)
                        manager.add_student(new_student)
                        manager.clear_console()

                        while True:
                            other_student = add_another_student()
                            if other_student == 'yes':
                                manager.clear_console()
                                aux_student = ask_student_information(manager)
                                manager.add_student(aux_student)
                                manager.clear_console()
                            elif other_student == 'no':
                                break
                            else:
                                invalid_nof()
                    case 2:
                        manager.clear_console()
                        list_tittle()
                        manager.read_students_list()
                        bk_opt = back_option(manager)

                        if bk_opt == 'yes':
                            continue
                        elif bk_opt == 'no':
                            break
                    case 3:
                        manager.clear_console()
                        average_list = manager.grades_average()
                        av_gd_tittle()
                        my_sorted_list = manager.sort_my_average_list(average_list)
                        manager.clear_console()
                        manager.read_average_list(my_sorted_list)
                        bk_opt = back_option(manager)

                        if bk_opt == 'yes':
                            continue
                        elif bk_opt == 'no':
                            break

                    case 4:
                        manager.clear_console()
                        manager.total_average()

                    case 5:
                        manager.clear_console()
                        manager.export_data()

                    case 6:
                        manager.clear_console()
                        manager.import_data()

                    case 7:
                        print("Exit...")
                        break
            else:
                print("Option out of range. Please enter a number between 1 and 7.")

                bk_opt = back_option(manager)
                if bk_opt == 'yes':
                    manager.clear_console()
                    continue
                elif bk_opt == 'no':
                    manager.clear_console()
                    break
                else:
                    invalid_nof()
                    continue   
        except ValueError:
            manager.clear_console()
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
