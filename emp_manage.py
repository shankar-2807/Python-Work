from employee import Employee

class EmployeeManage:
    def addEmp(self):
        id = int(input("Enter id:"))
        name = input("Enter name:")
        dept = input("Enter department:")
        sal = float(input("Enter salary:"))
        e1 = Employee(id, name, dept, sal)
        eData = str(e1)
        with open("Course/March_April/EMS/empDetails.txt", "a") as fp:
            fp.write(eData+"\n")
        print(f"{id} added successfully.")

    def updEmp(self):
        pass

    def delEmp(self):
        pass
    def searchEmp(self):
        pass
    def showAllEmp(self):
        pass

if(__name__ == "__main__"):
    em1 = EmployeeManage()
    em1.addEmp()

    