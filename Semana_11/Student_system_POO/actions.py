
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