# Creating a Bank Account
def CreateAccount():
    # OTP Password = nsiruyegnabfpawh
    # create database ABC_CBS;
    # use database ABC_CBS;
    # create table user_details(Aadhar bigint primary key, Mobile_No bigint, GMail_ID varchar(50), Password varchar(50), Name varchar(50), DateOfBirth date, Balance bigint default(0));
    import mysql.connector as spc
    c_o = spc.connect(host='localhost', user='toor', passwd='', database='test_project')
    cu = c_o.cursor()
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
            user_name = input("Please enter your name: ")
            user_dob = input("Please enter your Date of Birth (YYYY-MM-DD): ")
            # query = "insert into user_details values(%s, %s, '%s', '%s', '%s', '%s')" % (user_aadhar, user_mobile_no, user_gmail_id, user_passwd, user_name, user_dob)
            # cu.execute(query)
            print("Account created!")
            print()
            while True:
                choice_3 = input("Would you like to create another account? (Yes/No): ")
                if choice_3 == "Yes" or choice_3 == "yes":
                    break
                elif choice_3 == "No" or choice_3 == "no":
                    loop = False
                else:
                    print("Invalid choice. Please enter your choice again.")
                    print()
                    continue
        elif choice_2 == "No" or choice_2 == "no":
            break
        else:
            print("Invalid choice. Please enter your choice again.")


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
    print('''--------------------------------------------------------------------------------------------------------------
1. Create an Account
2. Log into an existing Account
3. Manage Account
4. Exit
--------------------------------------------------------------------------------------------------------------
    ''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        CreateAccount()

    elif choice == 2:
        break
    elif choice == 3:
        break
    elif choice == 4:
        break
    else:
        print()
        print("Invalid choice. Please select again:")
        print()
        print('''--------------------------------------------------------------------------------------------------------------
1. Create an Account
2. Log into an existing Account
3. Manage Account
4. Exit
--------------------------------------------------------------------------------------------------------------
        ''')
