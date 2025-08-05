class Employee:
    def __init__(self, id, name, dept, sal):
        self.eid = id
        self.ename = name
        self.dept = dept
        self.sal = sal

    def __str__(self):
        return f'{self.eid}, {self.ename}, {self.dept}, {self.sal}'

if(__name__ == "__main__"):
    e1 = Employee(101, "ABC XYZ", "Software Development", 35000.0)
    print(e1)

    