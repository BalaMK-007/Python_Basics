
def is_palindrome(teststr):
    #Using slice trick to reverse the string

    if teststr == teststr[::-1]:
        return True
    return False

run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit' : ")
    #if user types exits quit the program

    if teststr == 'exit':
        run = False
        break

    # Coverting string to lower
    teststr = teststr.lower()

    #Strip all the spaces and punctuation
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print("Palindorme test: ", is_palindrome(newstr))