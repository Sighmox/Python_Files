from dataclasses import dataclass


@dataclass
class Student:
    name: str
    college_id: int
    gpa: float




jeremy = Student('Jeremy', 55555, 3.1)
john = Student('John', 99494, 2.8)

print(jeremy)
print(john)
