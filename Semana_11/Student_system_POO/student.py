
class StudentObj:
    def __init__(self,name, group, spanish_score,english_score,social_score,science_score):
        self.name = name
        self.group = group
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.social_score = social_score
        self.science_score = science_score
    
    def __str__(self):
        return (f"Nombre: {self.name}, "
                f"Group:{self.group}, "
                f"Español:{self.spanish_score}, "
                f"Inglés: {self.english_score}, "
                f"Sociales:{self.social_score}, "
                f"Ciencias: {self.science_score}")
    
