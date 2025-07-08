import os
from menu import students_format

class StudentManager:
    def __init__(self):
        self.students = []

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_student(self, student):
        self.students.append(student)

    def get_students_list(self):
        return self.students

    def read_students_list(self):
        for student in self.students:
            students_format(student)

    def validate_input(self, opt):
        return 0 <= opt <= 100

    def get_spanish_grade(self, student):
        return student['spanish_grade']

    def get_english_grade(self,student):
        return student['english_grade']
    
    def get_social_grade(self, student):
        return student['social_grade']
    
    def get_science_grade(self,student):
        return student['science_grade']
    
    def grades_average(self):
        average_list = []
        for student in self.students:
            sp_grade = self.get_spanish_grade(student)
            en_grade = self.get_english_grade(student)
            soc_grade = self.get_social_grade(student)
            sc_grade = self.get_science_grade(student)

            average_grade = (sp_grade + en_grade + soc_grade + sc_grade) / 4

            average_list.append({
                "name": student['name'],
                "group": student['group'],
                "spanish_grade": sp_grade,
                "english_grade": en_grade,
                "social_grade": soc_grade,
                "science_grade": sc_grade,
                "average_grade": average_grade
            })

        return average_list
    
    def sort_my_average_list(self, my_list):
        n = len(my_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if my_list[j]['average_grade'] < my_list[j + 1]['average_grade']:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        return my_list

    def read_average_list(self, average_list):
        print('=========  Top 3 Student Average Grades  =========\n')

        for idx, student in enumerate(average_list[:3], start=1):
            name = student['name'].capitalize()
            group = student['group']
            avg = round(student['average_grade'], 2)

            print(f"#{idx} Name   : {name}")
            print(f"   Group  : {group}")
            print(f"   Average: {avg:.2f}\n")

            if idx < 3:
                print('-' * 42)

    def total_average(self):
        av = 0
        total_av = 0
        final_result = 0
        total = 0
        for student in self.grades_average():
            av = student['average_grade']
            total_av += av
        final_result = len(self.grades_average())
        total = total_av / final_result 
        print(f' Promedio Total: {total}')

        

