from datetime import date
from datetime import time
from datetime import datetime

def main():
    #Get today's date
    # today = date.today()
    # print("Today's date is", today)

    # # Print out date's individual components
    # print("Date components: ",today.day, today.month, today.year)

    # # retrive today's weekday (0=Monday, 6=Sunay)
    # print("Today's Weekday # is", today.weekday())
    # days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # print("Which is a ", days[today.weekday()])

    # Date time objects
    #Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is ", today)

    # Get the current time
    t = datetime.time(datetime.now())
    print("The current time is ",t)

# Run the function
if __name__ == "__main__":
    main()