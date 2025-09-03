from menu import MenuHandler
from student import StudentObj
from actions import studentHandler

def main():
    menu = MenuHandler()
    stuHandler = studentHandler()
    while True:
        menu.main_view()
        option = menu.user_option()
        if 1 <= option <= 7:
                match option:
                    case 1:
                        name = menu.ask_name()
                        group = menu.ask_group()
                        spanish_score = menu.ask_spanish_score()
                        english_score = menu.ask_english_score()
                        social_score = menu.ask_social_score()
                        science_score = menu.ask_science_score()
                        student = StudentObj(name, group, spanish_score, english_score, social_score, science_score)
                        
                        stuHandler.add_student_to_list(student)

                        while True:
                            response = menu.ask_for_another_student()
                            if response.lower() == 'yes':
                                name = menu.ask_name()
                                group = menu.ask_group()
                                spanish_score = menu.ask_spanish_score()
                                english_score = menu.ask_english_score()
                                social_score = menu.ask_social_score()
                                science_score = menu.ask_science_score()
                                aux_student = StudentObj(name, group, spanish_score, english_score, social_score, science_score)

                                stuHandler.add_student_to_list(aux_student)
                            elif response.lower() == 'no':
                                bk_opt = menu.back_option()
                                if bk_opt == 'yes':
                                    break
                                elif bk_opt == 'no':
                                    continue
                                else:
                                    print('Invalid option, try again')
                            else:
                                print('Invalid option, try again')
                    case 2:
                        my_list = stuHandler.get_students_list()
                        if not my_list:
                            print('=========== Empty List ===========')
                            bk_opt = menu.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Invalid Option')
                        else:
                            print('Estudiantes agregados:')
                            stuHandler.read_students_list(menu)
                            bk_opt = menu.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Invalid Option')
                    case 3:
                        my_list = stuHandler.get_students_list()
                        if not my_list:
                            print('=========== Empty List ===========')
                            bk_opt = menu.back_option()
                            if bk_opt == 'yes':
                                continue
                            elif bk_opt == 'no':
                                break
                            else:
                                print('Invalid Option')
                        else:
                           average_list = stuHandler.get_average_grades()
                           sorted_list = stuHandler.sort_my_average_list(average_list)
                           stuHandler.read_average_list(sorted_list)
                           if bk_opt == 'yes':
                                continue
                           elif bk_opt == 'no':
                                break
                           else:
                               print('Error')
                    case 4:
                       print('case 4')
                    case 5:
                       print('case 5')
                    case 6:
                        print('case 6')
                    case 7:
                        print("Exit...")
                        break
        else:
                print("Option out of range. Please enter a number between 1 and 7.")                   
    
if __name__ == '__main__':
    main()
