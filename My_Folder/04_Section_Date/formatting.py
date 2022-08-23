from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string 
    # Control codes.

    now = datetime.now()

    ## Date Formatting ##

    # for printing year only use %y/%Y
    print(now.strftime("The Current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))
    
    # %c - local's date and time, %x - local date, %X - local time
    print(now.strftime("Local date and time: %c"))
    print(now.strftime("Local date : %x"))
    print(now.strftime("Local time : %X"))


    # Format time
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
    print(now.strftime('Current time: %I:%M:%S %p'))
    print(now.strftime('24-Hour time: %H:%M'))


if __name__ == "__main__":
    main()