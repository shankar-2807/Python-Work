from emp_manage import EmployeeManage

em1 = EmployeeManage()
class Admin:
    def __init__(self):
        ch = 0
        while(ch != '6'):
            print('''Please select options from below:
            1. Add employee
            2. Update employee
            3. Delete employee
            4. Search employee
            5. Show all employee
            6. Exit''')
            ch = input("Enter choice:")
            if(ch == '1'):
                em1.addEmp()
                
            elif(ch == '2'):
                pass
            elif(ch == '3'):
                pass
            elif(ch == '4'):
                pass
            elif(ch == '5'):
                pass
            elif(ch == '6'):
                print("Thanks for choosing us!")
            else:
                print("Invalid choice...")