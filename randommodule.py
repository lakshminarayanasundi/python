#randommodule
#random module is used to generate random numbers in python,randint is used and this func is defind in random module.

#sample
'''import random
a=random.sample(range(10,50),10)
print(a)'''

#randint()
'''import random
a=random.randint(20,50)
print(a)'''

#choice()
'''import random
a=[10,40,50,70,80]
b=random.choice(a)
print(b)'''

#task
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid")'''

#calendar
'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''


#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"day is{b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

import random
import time
for i in range(10):
    a=random.randint(20,40)
    print(a)
    time.sleep(2)
