import mysql.connector as spc
co = spc.connect(host='localhost', user='toor', passwd='')


# Creating a Bank Account
def CreateAccount():
    # OTP Password = nsiruyegnabfpawh
    cu = co.cursor()
    # cu.execute("create database ABC_CBS;")
    cu.execute("use ABC_CBS;")
    # cu.execute("create table user_details(Aadhar bigint primary key, Mobile_No bigint, GMail_ID varchar(50), Password varchar(50), Name varchar(50), DateOfBirth date, Balance bigint default 0);")
    loop = True
    while loop:
        print()
        choice_2 = input("Would you like to create an Account? (Yes/No): ")
        print()
        if choice_2 == "Yes" or choice_2 == "yes":
            user_aadhar = int(input("Please enter your Aadhar Number (Must be 12-Digits): "))
            user_mobile_no = int(input("Please enter your Mobile Number (Must be 10-Digits): "))
            user_gmail_id = input("Please enter your G-Mail ID: ")
            while True:
                if OTPVerification(user_gmail_id):
                    print('OTP verified successfully.')
                    print()
                    break
                else:
                    print("OTP failed to verify. Please try again.")
                    continue
            while True:
                user_passwd = input("Please enter a strong password: ")
                user_passwd_r = input("Please enter your password again: ")
                if user_passwd == user_passwd_r:
                    break
                else:
                    print("Passwords don't match. Please try again.")
                    continue
            user_name = input("Please enter your Name: ")
            user_dob = input("Please enter your Date of Birth (YYYY-MM-DD): ")
            query = "insert into user_details values(%s, %s, '%s', '%s', '%s', '%s', 0)" % (user_aadhar, user_mobile_no, user_gmail_id, user_passwd, user_name, user_dob)
            cu.execute(query)
            print("Account created!")

            loop2 = True
            while loop2:
                print()
                choice_3 = input("Would you like to create another account? (Yes/No): ")
                if choice_3 == "Yes" or choice_3 == "yes":
                    break
                elif choice_3 == "No" or choice_3 == "no":
                    loop = False
                    loop2 = False
                else:
                    print("Invalid choice. Please enter your choice again.")
                    continue
        elif choice_2 == "No" or choice_2 == "no":
            break
        else:
            print("Invalid choice. Please enter your choice again.")
    co.commit()

# Logging into an Account
def LoginAccount():
    cu = co.cursor()
    cu.execute("use ABC_CBS;")
    cu.execute("select * from user_details;")
    data = cu.fetchall()
    loop = True
    logged_in = False
    while loop:
        count = 0
        print()
        temp_g = input("Please enter your G-Mail ID: ")
        temp_p = input("Please enter your password: ")
        print()
        for i in range(len(data)):
            if temp_g == data[i][2]:
                count = count + 1
        for i in range(len(data)):
            if count == 1:
                if temp_g == data[i][2] and temp_p == data[i][3]:
                    loop4 = True
                    while loop4:
                        if OTPVerification(temp_g):
                            print('OTP verified successfully.')
                            print()
                            print("Successfully logged in! Welcome back,", data[i][4])
                            logged_in = True
                            loop = False
                            loop4 = False
                        else:
                            print("OTP failed to verify. Please try again.")
                            continue
                    break
            elif count == 0:
                print("No Accounts found. Please try again.")
                break
            else:
                print("Accounts with the same email has been found. Please enter your Aadhar Number to continue.")
                loop2 = True
                while loop2:
                    print()
                    temp_a = int(input("Please enter your Aadhar Number: "))
                    for i in range(len(data)):
                        if temp_g == data[i][2] and temp_p == data[i][3] and temp_a == data[i][0]:
                            print()
                            print("Successfully logged in! Welcome back,", data[i][4])
                            logged_in = True
                            loop2 = False
                            break
                    else:
                        print()
                        print("Invalid Aadhar. Please try again.")
                        loop2 = False
                        continue
                break
        else:
            print("Wrong G-Mail/Password. Please try again.")
        if logged_in:
            ManageAccount(temp_g)
            print()
            loop3 = True
            while loop3:
                choice_2 = input("Do you wish to login to another account? (Yes/No): ")
                if choice_2 == 'Yes' or choice_2 == 'yes':
                    loop3 = False
                    continue
                elif choice_2 == 'No' or choice_2 == 'no':
                    loop = False
                    break
                else:
                    print("Invalid choice. Please try again.")
                    continue

def ManageAccount(t_g):
    cu = co.cursor()
    cu.execute("use ABC_CBS;")
    loop = True
    while loop:
        print()
        print("1. View Account Details")
        print("2. Deposit Money in Account")
        print("3. Change User Details")
        print("4. Exit")
        print()
        choice_2 = int(input("Enter your choice: "))
        if choice_2 == 1:
            cu.execute("select * from user_details;")
            data = cu.fetchall()
            count = 0
            for i in range(len(data)):
                if t_g == data[i][2]:
                    count = count + 1
            for i in range(len(data)):
                if t_g == data[i][2] and count == 1:
                    print()
                    print("Aadhar Number:", data[i][0])
                    print("Mobile Number:", data[i][1])
                    print("G-Mail ID:", data[i][2])
                    print("Name:", data[i][4])
                    print("Date Of Birth:", data[i][5])
                    print("Balance:", data[i][6])
                    break
                else:
                    print()
                    print("More than 2 Accounts found.")
                    t_a = int(input("Please enter your Aadhar Number: "))
                    for i in range(len(data)):
                        if t_g == data[i][2] and t_a == data[i][0]:
                            print()
                            print("Aadhar Number:", data[i][0])
                            print("Mobile Number:", data[i][1])
                            print("G-Mail ID:", data[i][2])
                            print("Name:", data[i][4])
                            print("Date Of Birth:", data[i][5])
                            print("Balance:", data[i][6])
                            break
                break






# OTP Verification
def OTPVerification(mail):
    import random
    import smtplib as smtp
    smtp = smtp.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('abcbank2022.3@gmail.com', 'nsiruyegnabfpawh')
    otp = random.randrange(100000, 999999)
    message = '''
Hello Customer,
    Greetings from ABC Bank. Hope you're having a good day.

Your OTP for verification is: ''' + str(otp)
    smtp.sendmail('abcbank2022.3@gmail.com', mail, message)
    print()
    print("OTP sent. Please check your mail.")
    iotp = int(input("Please enter the OTP sent in the given email: "))
    if iotp == otp:
        return True
    else:
        return False


print()
print("Welcome to ABC Bank, choose one of the options to get started:")
print()

while True:
    print()
    print('''--------------------------------------------------------------------------------------------------------------
1. Create an Account
2. Log into an existing Account
3. Exit
--------------------------------------------------------------------------------------------------------------
    ''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        CreateAccount()
    elif choice == 2:
        LoginAccount()
    elif choice == 3:
        break
    else:
        print()
        print("Invalid choice. Please select again:")