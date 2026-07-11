import datetime


print("***********This iS the Age Analyzer Program********")
uname = input("Enter Your Name: ")
dob = int(input("Enter your year of birth: "))

currentYear = datetime.datetime.now().year
age = currentYear - dob

print("Your Name is: ", uname)
print("By the end of this year you will be: ", age)

