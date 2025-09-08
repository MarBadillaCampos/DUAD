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
            if 1 <= option <= 7:
                match option:
                    case 1:
                       name = menu_handler.ask_name()
                       group = menu_handler.ask_group()
                       spanish_sc = menu_handler.ask_spanish_score()
                       english_sc = menu_handler.ask_english_score()
                       social_sc = menu_handler.ask_social_score()
                       science_sc = menu_handler.ask_science_score()
                       student_obj = student(name,group,spanish_sc,english_sc,social_sc,science_sc)
                       actions_handler.add_student(student_obj)

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
                               break
                           else: 
                                print('Error case 1') 
                    case 2:
                       actions_handler.read_student_list()
                    case 3:
                        three_average_list = actions_handler.sort_list()
                        actions_handler.read_average_list(three_average_list)
                    case 4:
                        actions_handler.total_average()
                        actions_handler.read_total_average()
                    case 5:
                        name = menu_handler.delete_name()
                        actions_handler.delete_student(menu_handler)
                    case 6:
                       student_dict = [s.to_dict() for s in actions_handler.student_list]
                       file_path = 'students.csv'
                       if student_dict:
                                headers = student_dict[0].keys()
                                data_handler.create_csv(file_path,headers)
                                data_handler.write_csv_file(file_path,headers, student_dict)

                    case 7:
                        print("Exit...")
                        break
            else:
                print("Option out of range. Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
           

if __name__ == '__main__':
    main()
