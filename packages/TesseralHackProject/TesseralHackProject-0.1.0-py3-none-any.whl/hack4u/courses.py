#! /usr/bin/env python3

class Course:

    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link
    
    def __repr__(self) -> str:
        return f"Nombre del curso: {self.name} :: duracion: {self.duration}"

courses = [
    Course("Introduccion al Inux", 15, "link1"),
    Course("Personalizacion del Inux", 3, "link2"),
    Course("Introdducion al X", 53, "link3")
]

def list_courses():

    for course in courses:
        print(course)

def search_course_by_name(name):
    for course in courses:
        if course.name == name:
            return course
    
    return None