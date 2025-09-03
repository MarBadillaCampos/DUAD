
class studentHandler:
    def __init__(self):
        self.student_list = []

    def add_student_to_list(self, student):
        self.student_list.append(student)
    
    def get_students_list(self):
        return self.student_list
    
    def read_student_from_list(self):
        for s in self.student_list:
            print(f"{s.name} - Group: {s.group} - Español: {s.spanish_score}, Inglés: {s.english_score}, Sociales: {s.social_score}, Ciencias: {s.science_score}")


    def get_average_grades(self):
        self.average_grades = []
        for student in self.student_list:
            sp_grade = student.spanish_score
            en_grade = student.english_score
            soc_grade = student.social_score
            sc_grade = student.science_score

            student.average_grade = int((sp_grade + en_grade + soc_grade + sc_grade) / 4)

            self.average_grades.append(student)

        return self.average_grades
    
    def sort_my_average_list(self, my_list):
        n = len(my_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if my_list[j].average_grade < my_list[j + 1].average_grade:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list
    
    def read_average_list(self, average_list):
        print('=========  Top 3 Student Average Grades  =========\n')
        for idx, student in enumerate(average_list[:3], start=1):
            name = student.name.capitalize()
            group = student.group
            avg = round(student.average_grade, 2)

            print(f"#{idx} Name   : {name}")
            print(f"   Group  : {group}")
            print(f"   Average: {avg:.2f}\n")

            if idx < 3:
                print('=' * 42)
                
    def read_students_list(self,menu):
        for student in self.student_list:
            menu.students_format(student)