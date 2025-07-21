from menu import MenuHandler
from actions import StudentManager 
from data import DataHandler

def main():
    manager = StudentManager() 
    exp_handler = DataHandler()
    menu_handler = MenuHandler()

    while True:
        menu_handler.menu()
        try: 
            option = menu_handler.user_option()
            if 1 <= option <= 7:
                match option:
                    case 1:
                        manager.clear_console()
                        new_student = menu_handler.ask_student_information(manager)
                        manager.add_student(new_student)
                        manager.clear_console()
                        while True:
                            other_student = menu_handler.add_another_student(manager)
                            if other_student == 'yes':
                                manager.clear_console()
                                aux_student = menu_handler.ask_student_information(manager)
                                manager.add_student(aux_student)
                                manager.clear_console()
                            elif other_student == 'no':
                                break
                            else:
                                menu_handler.invalid_nof()
                    case 2:
                        manager.clear_console()
                        my_list = manager.get_students_list()
                        if not my_list:
                            print('=========== Empty List ===========')
                            bk_opt = menu_handler.back_option(manager)

                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                menu_handler.invalid_nof() 
                        else:
                            menu_handler.list_tittle()
                            manager.read_students_list(menu_handler)
                            bk_opt = menu_handler.back_option(manager)
                            manager.clear_console()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                menu_handler.invalid_nof() 
                    case 3:
                        manager.clear_console()
                        average_list = manager.grades_average()
                        menu_handler.list_tittle()
                        my_sorted_list = manager.sort_my_average_list(average_list)
                        manager.clear_console()
                        manager.read_average_list(my_sorted_list)
                        bk_opt = menu_handler.back_option(manager)
                        manager.clear_console()
                        if bk_opt == 'yes':
                            continue
                        elif bk_opt == 'no':
                            break
                        else:
                            menu_handler.invalid_nof()
                    case 4:
                        manager.clear_console()
                        manager.total_average()
                        manager.read_total_average()
                        bk_opt = menu_handler.back_option(manager)
                        manager.clear_console()
                        if bk_opt == 'yes':
                            continue
                        elif bk_opt == 'no':
                            break
                        else:
                            menu_handler.invalid_nof()
                    case 5:
                        records_list = manager.grades_average()
                        file_path = 'students.csv'
                        manager.clear_console()

                        if records_list:
                            headers = records_list[0].keys()
                            exp_handler.create_csv(file_path,headers)
                            exp_handler.write_csv_file(file_path,headers, records_list)
                            bk_opt = menu_handler.back_option(manager)
                            manager.clear_console()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                menu_handler.invalid_nof()
                        else:
                            print("No hay datos para exportar.")
                    case 6:
                        manager.clear_console()
                        file_path = 'students.csv'
                        aux_list = exp_handler.read_csv_file_import(file_path)
                        delete_list = exp_handler.delete_item_from_list(aux_list)
                        for row in delete_list:
                            manager.add_student(row)
                        print("Information Imported")
                        bk_opt = menu_handler.back_option(manager)
                        manager.clear_console()
                        if bk_opt == 'yes':
                            continue
                        elif bk_opt == 'no':
                            break
                        else:
                            menu_handler.invalid_nof()
                    case 7:
                        print("Exit...")
                        break
            else:
                print("Option out of range. Please enter a number between 1 and 7.")

                bk_opt = menu_handler.back_option(manager)
                if bk_opt == 'yes':
                    manager.clear_console()
                    continue
                elif bk_opt == 'no':
                    manager.clear_console()
                    break
                else:
                    menu_handler.invalid_nof()
                    continue   
        except ValueError:
            manager.clear_console()
            print("Invalid input. Please enter a valid number.")
            bk_opt = menu_handler.back_option(manager)
            if bk_opt == 'yes':
                continue
            elif bk_opt == 'no':
                break
            else:
                menu_handler.invalid_nof()

if __name__ == '__main__':
    main()
