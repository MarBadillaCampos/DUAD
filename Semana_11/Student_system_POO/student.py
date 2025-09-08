
class student:
    def __init__(self,name, group, spanish_score,english_score,social_score,science_score):
        self.name = name
        self.group = group
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.social_score = social_score
        self.science_score = science_score
        self.average_grade = int((spanish_score + english_score + social_score + science_score)/4)
    
    def to_dict(self):
        return {
            "name": self.name,
            "group": self.group,
            "spanish_score": self.spanish_score,
            "english_score": self.english_score,
            "social_score": self.social_score,
            "science_score": self.science_score
        }
    

    