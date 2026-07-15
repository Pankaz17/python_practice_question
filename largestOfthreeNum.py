print("********* Finding the largest of Three Number*********")

num1 = int(input("Enter The value of first number: "))
num2 = int(input("Enter The value of second number: "))
num3 = int(input("Enter The value of third number: "))
largestNum = 0

if num1 >= num2 and num1 >= num3:
    largestNum = num1
elif num2 >= num3 and num2 >= num1:
    largestNum = num2
else:
    largestNum = num3

print("The largest number among you entered is: ", largestNum)
