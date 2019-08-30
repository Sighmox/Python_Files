class Student:
    def __init__ (self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, id: {self.college_id}, GPA: {self.gpa}"

joe = Student('Joe', 'ddd333ddd', '3.5')
mary = Student('Mary', 'eee356eee', '2.7')

print(joe)
print(mary)
