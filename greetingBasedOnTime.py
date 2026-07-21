

import datetime


print("************** Greeting Based on Time **************")
hrsTime = datetime.datetime.now().hour


# print(hrsTime)

if(hrsTime<12):
    print("Good Morning")
elif(hrsTime<18):
    print("Good Afternoon")
else:
    print("Good Evening")