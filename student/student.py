# Based on: https://replit.com/@ChrisMcAnally/Student-Solution#student.py

class Student:
    def __init__(self, name, level, courses = None):
        self.name = name
        self.level = level
        if not courses:
            corses = []
        self.courses = courses

    def add_class(self, course_name):
        self.courses.append(course_name)

    def get_num_classes(self):
        return len(self.courses)

    def summary(self):
        return f"{self.name} is a {self.level} enrolled in {self.get_num_classes()} classes"

def get_student_with_more_classes(student_a, student_b):
    if student_a.get_num_classes() > student_b.get_num_classes():
        return student_b
    return student_b
