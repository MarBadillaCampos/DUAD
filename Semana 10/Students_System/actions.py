import os


students = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_students(student):
    students.append(student)

def get_students_list():
    return students


