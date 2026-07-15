print("*******Sum Of the numbers From the list*********")

numList = []

listRange = int(input("Enter the range of the list you want: "))


for i in range(listRange):
    num = int(input(f"Enter the {i+1} number: "))
    numList.append(num)

totalSum = 0
for i in range(len(numList)):
    totalSum += numList[i]


print("The sum of the whole list without using sum( ) function is: ", totalSum)
