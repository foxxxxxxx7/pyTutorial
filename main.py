PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry",]

class Garden:
    def __init__(self, diagram, students= STUDENTS):
        self.row1, self.row2 = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        plants = self.row1[2*index:2*index+2] + self.row2[2*index:2*index+2]
        return [PLANTS[plant] for plant in plants]