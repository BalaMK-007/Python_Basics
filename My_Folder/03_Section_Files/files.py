# Files handling in python

def main ():

    #For open a file in write mode, it will create the file if it doesn't exist
    # myfile = open("textfile.txt","w+")

    # Appeding new text into the file
    # myfile = open("textfile.txt","a+")

    # # Writing inside the file
    # for i in range(10):
    #     myfile.write("Python is really so Cool\n")

    # #Close the file when done
    # myfile.close()

    # Reading and back up file contents
    myfile = open("textfile.txt","r")
    if myfile.mode == "r":
        # contents = myfile.read()
        # print(contents)
        fl = myfile.readlines()
        for x in fl:
            print(x)

# Run the function
if __name__ == "__main__":
    main()