print("******Odd Even Identifier*********")


num = int(input("Enter a number: "))


def isEven(a):
    if a%2== 0:
        return True
    else:
        return False
print("The number you entered is even?", isEven(num))