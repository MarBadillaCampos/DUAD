import os
class actionHandler:
    def __init__(self):
        self.student_list = []
    
    def add_student(self,student):
        return self.student_list.append(student)
    
    def get_student_list(self):
        return self.student_list
    
    def read_student_list(self,menu_handler):
        for student in self.student_list:
            menu_handler.students_format(student)

    def read_student_list_dos(self):
         for stu in self.student_list:
             print(f'Name: {stu.name}, Group: {stu.group}, Spanish Score: {stu.spanish_score}, English Score: {stu.english_score}, Social Studies Score: {stu.social_score}, Science Score: {stu.science_score}, Average Score: {stu.average_grade}')

    def sort_list(self):
        n = len(self.student_list)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.student_list[j].average_grade < self.student_list[j + 1].average_grade:
                    self.student_list[j],self.student_list[j + 1] = self.student_list[j + 1],self.student_list[j]

        return self.student_list
    
    
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
    
    def total_average(self):
        av = 0
        total_av = 0
        final_result = 0
        total = 0
        try: 
            for student in self.student_list:
                av = student.average_grade
                total_av += av
            final_result = len(self.student_list)
            total = total_av / final_result 
            return total
        except ZeroDivisionError as e:
            print(f'Error {e}')
            return None
            
    
    def read_total_average(self):
        avg = round(self.total_average(), 2)
        print('========= Overall Student Performance =========\n')
        print(f' Total Average Grade: {avg:.2f}')


    def delete_student(self, delete_name, delete_group):
        for student in self.get_student_list():
            if student.name == delete_name and student.group == delete_group:
                self.student_list.remove(student)
                print(f'Deleted Student :  Name: {student.name} Group: {student.group}')
                break
        else:
            print('Student not found')


    
    def failed_students(self):
        failed_stu = []
        for student in self.student_list:
            failed_subjects = []  

            if student.spanish_score < 60:
                failed_subjects.append(("Spanish", student.spanish_score))
            if student.english_score < 60:
                failed_subjects.append(("English", student.english_score))
            if student.social_score < 60:
                failed_subjects.append(("Social", student.social_score))
            if student.science_score < 60:
                failed_subjects.append(("Science", student.science_score))

            if failed_subjects:  
                failed_stu.append((student, failed_subjects))
        
        return failed_stu

    
    def read_failed_student_list(self, failed_stu):
        for stu, subjects in failed_stu:
            print(f"\nName: {stu.name}, Group: {stu.group}")
            print("  Failed subjects:")
            for subj, score in subjects:
                print(f"    - {subj}: {score}")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    
    def student_exist(self, delete_name, delete_group):
        for student in self.get_student_list():
            if student.name == delete_name and student.group == delete_group:
                return True
        return False

                
    
