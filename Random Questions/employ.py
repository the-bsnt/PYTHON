class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"role = {self.role}")
        print(f"dept= {self.dept}")
        print(f"salary = {self.salary}")


class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("engineer", "mathematics", 185000)
        self.name = name
        self.age = age

    def show_details(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        super().show_details()
        return


E1 = Engineer("basnet", 26)
E1.show_details()
