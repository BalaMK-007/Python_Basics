
def main ():
    x = 0

    # While Loop
    # while (x<5):
    #     print(x)
    #     x = x + 1

    #For Loop
    # for x in range (5, 10):
    #     print(x)

    #Using for loop over a collection
    # days = ["Mon", "Tue", "Wed", "Thu", "Fri","Sat","Sun"]
    # for d in days:
    #     print(d)

    # Break and Continue Statements
    # for x in range (5, 10):
        # if x == 7:
        #     break # It will break the flow of loop and only print 5 6
        # if x % 2 == 0:
        #     continue # It will neglect 6 and 8 and print all other number upto 9, becuase the modulus of 6 and 8 with 2 is 0.
        # print(x)   

    # enumerate() Function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri","Sat","Sun"]
    for i,d in enumerate(days):
        print(i, d) # It will print the index of the values and the values. enumerate is used for getting index.


# Calling the function
if __name__ == "__main__":
    main()