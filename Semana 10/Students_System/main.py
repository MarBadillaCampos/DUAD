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
                        my_list = manager.get_students_list()
                        if not my_list:
                            print('=========== Empty List ===========')
                            bk_opt = back_option(manager)

                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                invalid_nof() 
                        else:
                            list_tittle()
                            manager.read_students_list()
                            bk_opt = back_option(manager)

                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                invalid_nof() 
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
                        else:
                            invalid_nof()
                    case 4:
                        manager.clear_console()
                        manager.total_average()
                        manager.read_total_average()
                        manager.clear_console()
                    case 5:
                        records_list = manager.grades_average()
                        file_path = 'students.csv'
                        manager.clear_console()

                        if records_list:
                            headers = records_list[0].keys()
                            manager.create_csv(file_path, headers)
                            manager.write_csv_file(file_path, headers, records_list)
                        else:
                            print("No hay datos para exportar.")
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
            bk_opt = back_option(manager)
            if bk_opt == 'yes':
                continue
            elif bk_opt == 'no':
                break
            else:
                invalid_nof()

if __name__ == '__main__':
    main()
