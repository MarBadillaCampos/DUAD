import os
from menu import students_format


students = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_students(student):
    students.append(student)

def get_students_list():
    return students

def read_Students_list():
    for student in get_students_list():
             students_format(student)


         

        
