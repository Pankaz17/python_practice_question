print("*********** This program will print Fizz, if the number is multiple of 3 print fizz, multiple of 5 print buzz and multiple of 3 and 5 print fizbuz ***********")



for i in range(1, 51):
    print(i, )
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i% 3 == 0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")