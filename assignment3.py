print(".......This is the program that Says how much should one person pay for meal in the group of friends........")
noOfPeople = int(input("Enter the number of people in the group....."))
billAmount = float(input("enter the amount of bill......"))

eachToPay = billAmount / noOfPeople

print("Each person should pay:", eachToPay)