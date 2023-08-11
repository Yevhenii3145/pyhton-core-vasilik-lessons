# Реализуйте класс для работников

class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print(f"Всего работников: {Employee.emp_count}")

    def display_employee(self):
        print(f"Name: {self.name} - Salary: {self.salary}")


emp_1 = Employee("Ivan", 25_000)
emp_2 = Employee("Olga", 55_000)
emp_1.display_employee()  # Name: Ivan - Salary: 25000
emp_2.display_employee()  # Name: Olga - Salary: 55000

print(Employee.emp_count)  # 2
print(emp_1.emp_count)  # 2
emp_1.display_count()  # Всего работников: 2
emp_2.display_count()  # Всего работников: 2
