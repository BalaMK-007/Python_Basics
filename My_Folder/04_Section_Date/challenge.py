import calendar

def countdays(theyear, themonth, whichday):
    daycount = 0
    weeklist = calendar.monthcalendar(theyear, themonth)
    for week in weeklist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

print("Day counter program")

run = True
while(run):
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or exit to quit")

        theday = input("?")
        if theday == "exit":
            run = False
            break
        day = int(theday)

        yearstr = input("Enter year: ")
        year = int(yearstr)

        monthstr = input("Enter Month: ")
        month = int(monthstr)

        result = countdays(year, month, day)
        print("There are " + str(result) + " of those day in month and year specified" )
        print("-----------\n")
    except Exception as e:
        print(e)
        print("Sorry, thatls not a vaild input")
    