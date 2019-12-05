# database
db_email = "ssajolbd50@gmail.com"
db_password = "55555"

# input email from prompt
email = input("Enter Your Email  : ")

# varification procces start here
if email == db_email:
    # verify password
    password = input("Enter Your PAssword : ")
    if password == db_password:
        print("You are in sourojogot ")
    else:
        print("Your password is not valid ")
else:
    print("Your email is not valid ")
