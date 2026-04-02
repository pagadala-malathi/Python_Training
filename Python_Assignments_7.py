
#Task-1

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

s = Student("maha", 1, "CSE", 60000)
f = Faculty("prof.Balaji", 101, 50000)
t = TempFaculty("lakshmi", 102, 40000, "6 months")

print("Student:", s.name, s.id, s.dept, s.fees)
print("Faculty:", f.name, f.id, f.salary)
print("TempFaculty:", t.name, t.id, t.salary, t.duration)


# Task-2

from abc import ABC, abstractmethod

class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
        
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}"
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

s = Student("maha", 1, "CSE", 60000)
f = Faculty("prof.Balaji", 101, 50000)
t = TempFaculty("Lakshmi", 102, 40000, "6 months")
print(s.get_details())
print(f.get_details())
print(t.get_details())

# Task-3

class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
    def get_details(self):
        return f"{self.name}, {self.id}, {self.dept}, Fees: {self.fees}"
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
    def get_details(self):
        return f"{self.name}, {self.id}, Salary: {self.salary}"
students = [
    Student("maha", 1, "CSE", 60000),
    Student("keerthi", 2, "ECE", 40000),
    Student("Azeem", 3, "IT", 70000)]
faculty = [
    Faculty("Lakshmi", 101, 50000),
    Faculty("malathi", 102, 28000),
    Faculty("devi", 103, 35000)]
students.sort(key=lambda x: x.fees)

print("Students Sorted by Fees")
for s in students:
    print(s.get_details())
faculty.sort(key=lambda x: x.salary)
print("\n Faculty Sorted by Salary ")
for f in faculty:
    print(f.get_details())

#Task 4

class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
students = [
    Student("maha", 1, "CSE", 60000),
    Student("keerthi", 2, "ECE", 40000),
    Student("Azeem", 3, "IT", 70000)]
names = list(map(lambda s: s.name, students))
print("Student Names:", names) 

#Task-5

class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"{self.name}, Fees: {self.fees}"

class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return f"{self.name}, Salary: {self.salary}"
students = [
    Student("maha", 1, "CSE", 60000),
    Student("keerthi", 2, "ECE", 40000),
    Student("Azeem", 3, "IT", 70000)]
faculty = [
    Faculty("Lakshmi", 101, 50000),
    Faculty("malathi", 102, 28000),
    Faculty("Devi", 103, 35000)]

highest_fee_students = list(filter(lambda s: s.fees > 50000, students))

highest_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print(" Students with Fees > 50000 ")
for s in highest_fee_students:
    print(s.get_details())

print("\n Faculty with Salary > 30000 ")
for f in highest_salary_faculty:
    print(f.get_details())

# Task-6

from functools import reduce
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

students = [
    Student("maha", 1, "CSE", 60000),
    Student("keerthi", 2, "ECE", 40000),
    Student("Azeem", 3, "IT", 70000)]

faculty = [
    Faculty("Lakshmi", 101, 50000),
    Faculty("Malathi", 102, 28000),
    Faculty("Devi", 103, 35000)]

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees Collected:", total_fees)
print("Total Salary Paid:", total_salary)

#Task-7: Higher Order Function

class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Maha", 1, "CSE", 60000),
    Student("keerthi", 2, "ECE", 40000),
    Student("Azeem", 3, "IT", 70000)]

names = process_users(students, lambda s: s.name)

fees = process_users(students, lambda s: s.fees)
print("Names:", names)
print("Fees:", fees)


# Final Challenge:

from abc import ABC, abstractmethod
from functools import reduce

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = int(fees)

    def get_details(self):
        return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = int(salary)

    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"{super().get_details()}, Duration: {self.duration}"

students = [
    Student("maha", 1, "CSE", 60000),
    Student("keerthi", 2, "ECE", 40000),
    Student("Azeem", 3, "IT", 70000)]

faculty = [
    Faculty("Lakshmi", 101, 50000),
    Faculty("Malathi", 102, 28000),
    TempFaculty("Devi", 103, 35000, "6 months")]

print("\nAll Students ")
for s in students:
    print(s.get_details())

print("\nAll Faculty ")
for f in faculty:
    print(f.get_details())

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\n Sorted Students (by Fees)")
for s in students:
    print(s.get_details())

print("\nSorted Faculty (by Salary)")
for f in faculty:
    print(f.get_details())

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nFiltered Students (Fees > 50000)")
for s in high_fee_students:
    print(s.get_details())

print("\n Filtered Faculty (Salary > 30000)")
for f in high_salary_faculty:
    print(f.get_details())

names = list(map(lambda s: s.name, students))
print("\nStudent Names:", names)

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)











    





