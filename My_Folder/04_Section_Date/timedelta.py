from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from socket import AF_DECnet

# Construct a basic timedelta and print it
# print(timedelta(days = 365, hours = 5, minutes = 1))

# #Print today's date
# now = datetime.now()
# print("Today is", now)

# # Using timedelta to print date one year from now
# print("One year from now it will be", str(now + timedelta(days = 365)))

# # Timedelta that uses more than one argument.
# print("In two weeks and three days it will be", str(now + timedelta(weeks=2, days=3)))

# # calculating the date 1 week age, formated as a string
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d,%Y")
# print("One week age it was ", s)

# How many days until april fools day?
today = date.today()
afd = date(today.year, 4, 1)

#Date comparison to see if april fool's day has already gone for this year
# If it has, use the replace() function to get the date for next year

if afd < today:
    print("April Fools day already went by: ", ((today-afd).days))
    afd = afd.replace(year = today.year + 1)

    # Calculate amount of days left for april fool day
time_to_afd = afd - today
print("It is", time_to_afd.days, "days untill the next April Fools' Day!")

