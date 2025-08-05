from admin import Admin

ch = 0
while(ch != '2'):
    print('''Please select choice from below:
    1. Login
    2. Exit''')
    ch = input("Enter choice:")
    if(ch == '1'):
        uname = input("Enter username:")
        passw = input("Enter password:")
        if(uname == 'admin' and passw == "1234"):
            print("Welcome admin")
            ad1 = Admin()
        else:
            print("Invalid credentials...")
    elif(ch == '2'):
        print("Thank you for visiting!")
    else:
        print("Invalid choice...")

        