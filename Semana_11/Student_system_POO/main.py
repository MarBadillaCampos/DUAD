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
                        spanish_score = menu.ask_spanish_score()
                        english_score = menu.ask_english_score()
                        social_score = menu.ask_social_score()
                        science_score = menu.ask_science_score()
                        student = StudentObj(name, spanish_score, english_score, social_score, science_score)
                        
                        stuHandler.add_student_to_list(student)

                        while True:
                            response = menu.ask_for_another_student()
                            if response.lower() == 'yes':
                                name = menu.ask_name()
                                spanish_score = menu.ask_spanish_score()
                                english_score = menu.ask_english_score()
                                social_score = menu.ask_social_score()
                                science_score = menu.ask_science_score()
                                aux_student = StudentObj(name, spanish_score, english_score, social_score, science_score)

                                stuHandler.add_student_to_list(aux_student)

                            elif response.lower() == 'false':
                                break
                            else:
                                print('Invalid option, try again')

                        print('Estudiantes agregados:')
                        for s in stuHandler.student_list:
                            print(f"{s.name} - Español: {s.spanish_score}, Inglés: {s.english_score}, Sociales: {s.social_score}, Ciencias: {s.science_score}")

                    case 2:
                       print('case 2')
                    case 3:
                        print('case 3')
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
