class School:
    def __init__(self):
        self.students = {}
        self.results = []

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []

        if any(name in students for students in self.students.values()):
            self.results.append(False)
        else:
            self.students[grade].append(name)
            self.results.append(True)

    def roster(self):
        all_students = []
        for grade in sorted(self.students.keys()):
            all_students.extend(sorted(self.students[grade]))
        return all_students

    def grade(self, grade):
        if grade in self.students:
            return sorted(self.students[grade])
        else:
            return []

    def added(self):
        return self.results
