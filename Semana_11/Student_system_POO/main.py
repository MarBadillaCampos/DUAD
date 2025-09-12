from menu import menuHandler
from student import student
from actions import actionHandler
from data import DataHandler

def main():
    menu_handler = menuHandler()
    actions_handler = actionHandler()
    data_handler = DataHandler()


    while True:
        menu_handler.menu()
        try: 
            option = menu_handler.user_option()
            if 1 <= option <= 9:
                match option:
                    case 1:
                       actions_handler.clear_console()
                       name = menu_handler.ask_name()
                       group = menu_handler.ask_group()
                       spanish_sc = menu_handler.ask_spanish_score()
                       english_sc = menu_handler.ask_english_score()
                       social_sc = menu_handler.ask_social_score()
                       science_sc = menu_handler.ask_science_score()
                       student_obj = student(name,group,spanish_sc,english_sc,social_sc,science_sc)
                       actions_handler.add_student(student_obj)
                       actions_handler.clear_console()
                       while True:
                           user_option = menu_handler.add_other_student()
                           if user_option == 'yes':
                                    name = menu_handler.ask_name()
                                    group = menu_handler.ask_group()
                                    spanish_sc = menu_handler.ask_spanish_score()
                                    english_sc = menu_handler.ask_english_score()
                                    social_sc = menu_handler.ask_social_score()
                                    science_sc = menu_handler.ask_science_score()
                                    other_stu_obj = student(name,group,spanish_sc,english_sc,social_sc,science_sc)
                                    actions_handler.add_student(other_stu_obj)      
                           elif user_option == 'no':
                               opt = menu_handler.back_option()
                               if opt == 'yes':
                                   break
                               elif opt == 'no':
                                   continue
                               else:
                                   print('Error')
                           else: 
                                print('Invalid Input') 
                    case 2:
                        my_list = actions_handler.get_student_list()
                        if not my_list:
                            print('=========== Empty List ===========')
                            bk_opt = menu_handler.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Error')
                        else:
                            actions_handler.clear_console()
                            actions_handler.read_student_list(menu_handler)
                            bk_opt = menu_handler.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Error')
                    case 3:
                        three_average_list = actions_handler.sort_list()
                        if not three_average_list:
                            print('=========== Empty Average Grade List ===========')
                            bk_opt = menu_handler.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Error')
                        else:
                            actions_handler.clear_console()
                            actions_handler.read_average_list(three_average_list)
                            bk_opt = menu_handler.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Error')
                    case 4:
                        my_list = actions_handler.get_student_list()
                        if not my_list:
                            print('=========== Empty Global Average ===========')
                            bk_opt = menu_handler.back_option()

                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Error')
                        else: 
                            average = actions_handler.total_average()
                            if average is not None:
                                actions_handler.read_total_average()
                            bk_opt = menu_handler.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':

                                break
                            else:
                                print('Error')
                    case 5:
                        delete_name = menu_handler.ask_for_delete_name()
                        actions_handler.delete_student(delete_name)
                    case 6:
                       student_dict = [s.to_dict() for s in actions_handler.student_list]
                       file_path = 'students.csv'
                       if student_dict:
                                headers = student_dict[0].keys()
                                data_handler.create_csv(file_path,headers)
                                data_handler.write_csv_file(file_path,headers, student_dict)
                    case 7:
                        file_path = 'students.csv'
                        aux_list = data_handler.read_csv_file_import(file_path)
                        if aux_list:
                            delete_list = data_handler.delete_item_from_list(aux_list)
                            for row in delete_list:
                                stu_obj = student(
                                    row['name'],
                                    row['group'],
                                    row['spanish_score'],
                                    row['english_score'],
                                    row['social_score'],
                                    row['science_score']
                                )
                                actions_handler.add_student(stu_obj)
                            print("Import Completed")
                            
                        else:
                          print('Error')
                    case 8:
                        failed_stu = actions_handler.failed_students()
                        actions_handler.read_failed_student_list(failed_stu)
                    case 9:
                        print("Exit...")
                        break
            else:
                print("Option out of range. Please enter a number between 1 and 9.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
           

if __name__ == '__main__':
    main()
